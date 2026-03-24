import os
from google.adk import Agent
import agent.settings as settings
from agent.model_armor_guard import create_model_armor_guard


model_armor_guard = create_model_armor_guard(
    project_id=settings.PROJECT_ID,
    template_name=settings.FULL_TEMPLATE_NAME,
    location=settings.LOCATION
)

simple_agent = Agent(
    name="say_hi",
    model=settings.GEMINI_MODEL,
    instruction="""Find creative ways to greet the user.""",
    before_model_callback=model_armor_guard.before_model_callback,
    after_model_callback=model_armor_guard.after_model_callback,
)

root_agent = simple_agent
