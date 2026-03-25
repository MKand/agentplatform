# Challenge 4: MCP Tool Integration - Solution

## What We Added

An MCP (Model Context Protocol) server to extend agent capabilities with external tools.

## New Components

### MCP Server (`fun-fact-mcp-server/`)

A standalone FastMCP server deployed to Cloud Run:

```python
from fastmcp import FastMCP

mcp = FastMCP("Fun Fact Server")

@mcp.tool()
def get_fun_fact() -> str:
    """Returns a fun trivia fact."""
    return random.choice(facts)
```

### MCP Tool Integration in Agent

```python
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams

fun_fact_mcp_tool = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=settings.FUN_FACT_MCP_URL,
        headers={"Authorization": f"Bearer {get_bearer_token(settings.FUN_FACT_MCP_URL)}"},
    )
)

simple_agent = Agent(
    ...
    tools=[fun_fact_mcp_tool]
)
```

### Authentication (`fun_agent/auth.py`)

Service-to-service authentication using ID tokens:

```python
def get_bearer_token(audience: str) -> str:
    request = Request()
    return google.oauth2.id_token.fetch_id_token(request, audience)
```

## Deployment Method: Source Files

This solution uses **source file deployment** - deploying from source code instead of passing the agent object:

```python
remote_agent = client.agent_engines.create(
    config={
        "source_packages": ["./fun_agent"],
        "entrypoint_module": "fun_agent.agent",
        "entrypoint_object": "root_agent",
        "class_methods": [...],
    }
)
```

### Why Source Deployment?

**Agent object deployment (Challenge 3) uses pickle serialization**, which fails when the agent contains non-picklable objects. The `MCPToolset` contains:
- Stream connections that can't be serialized
- HTTP client objects
- File handles or logging handlers

**Source deployment** avoids this by:
1. Uploading source code as a `.tar.gz` archive
2. Agent Engine installs dependencies and runs the code directly
3. No pickle serialization needed

### When to Use This Method

- Agents with complex objects (MCP tools, database connections, etc.)
- Production deployments
- CI/CD pipelines
- When you need reproducible builds

## Deployment Steps

### 1. Deploy MCP Server to Cloud Run

First, authenticate:
```bash
gcloud auth login
gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT
```

**With Authentication (recommended for production):**
```bash
gcloud run deploy fun-fact-mcp-server \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$LOCATION \
  --memory=1Gi \
  --no-allow-unauthenticated \
  --set-env-vars=GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT \
  --source fun-fact-mcp-server
```

**Without Authentication (for testing/development):**
```bash
gcloud run deploy fun-fact-mcp-server \
  --project=$PROJECT_ID \
  --region=$LOCATION \
  --memory=1Gi \
  --allow-unauthenticated \
  --set-env-vars=GOOGLE_CLOUD_PROJECT=$PROJECT_ID \
  --source fun-fact-mcp-server
```

Note the resulting URL: `https://fun-fact-mcp-server-xxxx-uc.a.run.app`

### 2. Update Environment Variables

Update `fun_agent/.env` with your MCP server URL:
```bash
FUN_FACT_MCP_URL=https://fun-fact-mcp-server-xxxx-uc.a.run.app
```

### 3. Deploy Agent

Run the deployment script:

```bash
cd solutions/04-mcp-server
python3 deploy.py
```

## How MCP Works

1. Agent determines it needs to call `get_fun_fact`
2. ADK sends request to MCP server via HTTP
3. MCP server executes the function
4. Result returned to agent
5. Agent incorporates result into response

## Architecture

```
User → Agent Engine → Agent (ADK)
                      ↓
                  MCP Toolset
                      ↓
              MCP Server (Cloud Run)
                      ↓
                get_fun_fact()
```

## Testing

After deployment, try:
- "Tell me a fun fact"
- "Give me some trivia"

The agent should call the MCP tool and return a random fact.
