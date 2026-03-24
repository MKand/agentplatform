# Challenge 1: Simple Agent - Solution

## What We Built

A basic ADK agent that greets users creatively.

## Key Components

### `fun_agent/settings.py`
Configuration file with environment variables:
```python
GEMINI_MODEL = "gemini-2.5-flash"
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
```

### `fun_agent/agent.py`
The agent definition:
```python
from google.adk import Agent
import agent.settings as settings

simple_agent = Agent(
    name="say_hi",
    model=settings.GEMINI_MODEL,
    instruction="Find creative ways to greet the user.",
)

root_agent = simple_agent
```

## How to Run

```bash
# Set environment variables
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1
export GOOGLE_GENAI_USE_VERTEXAI=TRUE

# Run the agent
adk web
```

## Key Concepts

1. **`root_agent`**: ADK looks for this specific variable name to identify your agent
2. **Model selection**: Using `gemini-2.5-flash` for fast, cost-effective responses
3. **Instructions**: Natural language prompt that guides agent behavior

## Next Steps

Proceed to Challenge 2 to add security with Model Armor.
