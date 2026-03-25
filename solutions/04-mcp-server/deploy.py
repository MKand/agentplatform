import sys
import vertexai
import os
from pathlib import Path

project = os.getenv("GOOGLE_CLOUD_PROJECT")
mcp_server_url = os.getenv("FUN_FACT_MCP_URL")

client = vertexai.Client(
    project=project,
    location='us-central1',
)

def deploy_agent():
    """Deploys the Fun Agent with MCP Tooling."""
    print("Starting deployment to Vertex AI Agent Engine...")
    
    remote_agent = client.agent_engines.create(
        config={
            "display_name": "Fun agent with Facts",
            "description": "An agent deployed from source files with MCP tools",
            "source_packages": ["./fun_agent"],
            "entrypoint_module": "fun_agent.agent",
            "entrypoint_object": "root_agent",
            "requirements_file": "requirements.txt",
            "class_methods": [
                {
                    "name": "query",
                    "api_mode": "",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "user_input": {"type": "string"}
                        },
                        "required": ["user_input"]
                    }
                }
            ],
            "env_vars": {
                "FUN_FACT_MCP_URL": mcp_server_url
            }
        },
    )
    print(f"✅ Successfully deployed agent: {remote_agent.resource_name}")

if __name__ == "__main__":
    deploy_agent()
