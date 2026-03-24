
import os
from google.adk import Agent
from agent.model_armor_guard import create_model_armor_guard
from agent.auth import get_bearer_token
import agent.settings as settings
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams


fun_fact_mcp_tool = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=settings.FUN_FACT_MCP_URL,
        headers={"Authorization": f"Bearer {get_bearer_token(settings.FUN_FACT_MCP_URL)}"},
    ))

model_armor_guard = create_model_armor_guard(
    project_id=settings.PROJECT_ID,
     template_name=settings.FULL_TEMPLATE_NAME, 
     location=settings.LOCATION)

simple_agent = Agent(
    name="say_hi",
    model=settings.GEMINI_MODEL,
    instruction="""
    Say hi to the user. Use the 'fun_fact_mcp_tool' if they ask for a fun fact.
    """,
    before_model_callback=model_armor_guard.before_model_callback,
    after_model_callback=model_armor_guard.after_model_callback,
    tools=[fun_fact_mcp_tool]
)

root_agent = simple_agent

