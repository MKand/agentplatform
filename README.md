# ADK Intro Challenge

Build a production-ready agent with Google Agent Development Kit (ADK).

## Prerequisites

- Python 3.10+
- Google Cloud account with billing enabled
- `gcloud` CLI authenticated

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Authenticate
gcloud auth application-default login
```

## Challenges

### Challenge 1: Simple Agent
Create a greeting agent using the ADK.

**What you need to do:**
- Initialize an ADK Agent
- Choose and configure a model
- Add a greeting instruction
- Run the agent locally to verify it works

**Verify:** `adk web` starts and the agent responds to greetings.

---

### Challenge 2: Model Armor Security
Add security guardrails to detect prompt injection and sensitive data.

**What you need to do:**
- Create a Model Armor template via the Google Cloud Console or API
- Create callback functions that intercept LLM requests/responses
- Integrate the callbacks with your agent
- Test against: prompt injection attempts, credit card numbers, malicious URLs

**Verify:** Attack prompts are blocked with appropriate messages.

---

### Challenge 3: Deploy to Agent Engine
Deploy your agent as a cloud-hosted web service with observability.

**What you need to do:**
- Enable Agent Engine API in your project
- Configure telemetry (Cloud Monitoring)
- Set up agent identity for service accounts
- Create and run the deployment script

**Verify:** Agent is accessible via the Agent Engine endpoint.

---

### Challenge 4: MCP Tool Integration
Add an MCP server to extend your agent's capabilities.

**What you need to do:**
- Create a simple MCP server with at least one tool
- Deploy the MCP server to Cloud Run
- Integrate the MCP server as a tool in your agent
- Ensure authentication works between agent and MCP server

**Verify:** Agent can call the MCP tool and return results.

---

## Environment Variables

```bash
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=TRUE
TEMPLATE_NAME=your-model-armor-template
FUN_FACT_MCP_URL=https://your-mcp-server.run.app
```

## Solutions

The `solutions/` folder contains the completed code after each challenge:
- `solutions/01-simple-agent/` - Challenge 1 complete
- `solutions/02-model-armor/` - Challenge 2 complete
- `solutions/03-deploy/` - Challenge 3 complete
- `solutions/04-mcp-server/` - All challenges complete
