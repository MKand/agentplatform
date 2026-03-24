import vertexai
from vertexai import types
import os

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")

vertexai.init(project=PROJECT_ID, location=LOCATION)

env_vars_deploy = {
    "GOOGLE_GENAI_USE_VERTEXAI": "TRUE",
    "GOOGLE_CLOUD_PROJECT": PROJECT_ID,
    "GOOGLE_CLOUD_LOCATION": "us-central1",
}

def deploy():
    try:
        remote_agent = agent_engines.create(
            source_packages=["./fun_agent"],
            entrypoint_module="fun_agent.agent",
            entrypoint_object="root_agent",
            requirements_file="requirements.txt",
            display_name="fun_agent",
            identity_type=types.IdentityType.AGENT_IDENTITY,
            agent_framework="google-adk",
        )
        print(f"Deployed agent: {remote_agent}")
    except Exception as e:
        print(f"Unable to deploy agent: {e}")

if __name__ == "__main__":
    deploy()

