import os
from google.adk import Agent
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams
import agent.settings as settings
from agent.model_armor_guard import create_model_armor_guard
from agent.auth import get_bearer_token


model_armor_guard = create_model_armor_guard(
    project_id=settings.PROJECT_ID,
    template_name=settings.FULL_TEMPLATE_NAME,
    location=settings.LOCATION
)

token = get_bearer_token(settings.FUN_FACT_MCP_URL)
fun_fact_mcp_tool = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=settings.FUN_FACT_MCP_URL,
        headers={"Authorization": f"Bearer {token}"} if token else {},
    )
)

simple_agent = Agent(
    name="say_hi",
    model=settings.GEMINI_MODEL,
    instruction="""Say hi to the user. Use the 'get_fun_fact' tool if they ask for a fun fact.""",
    before_model_callback=model_armor_guard.before_model_callback,
    after_model_callback=model_armor_guard.after_model_callback,
    tools=[fun_fact_mcp_tool]
)

root_agent = simple_agent
