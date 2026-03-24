from google.adk import Agent
import fun_agent.settings as settings


simple_agent = Agent(
    name="say_hi",
    model=settings.GEMINI_MODEL,
    instruction="""Find creative ways to greet the user.""",
)

root_agent = simple_agent
