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

## Deployment Steps

### 1. Deploy MCP Server to Cloud Run

```bash
gcloud run deploy fun-fact-mcp-server \
  --project=$PROJECT_ID \
  --region=$LOCATION \
  --memory=1Gi \
  --no-allow-unauthenticated \
  --set-env-vars=GOOGLE_CLOUD_PROJECT=$PROJECT_ID \
  --source fun-fact-mcp-server
```

Note the resulting URL: `https://fun-fact-mcp-server-xxxx-uc.a.run.app`

### 2. Deploy Agent

```bash
export FUN_FACT_MCP_URL=https://fun-fact-mcp-server-xxxx-uc.a.run.app
python deploy.py
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
