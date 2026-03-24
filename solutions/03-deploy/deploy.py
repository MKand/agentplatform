import vertexai
# from vertexai import types
from vertexai.agent_engines import AdkApp
from fun_agent.agent import root_agent as agent


client = vertexai.Client(project="qwiklabs-gcp-00-dda2789fab10", location="us-central1")

env_vars_deploy = {
    "GOOGLE_GENAI_USE_VERTEXAI": "TRUE",
    "GOOGLE_CLOUD_PROJECT": "qwiklabs-gcp-00-dda2789fab10",
    "GOOGLE_CLOUD_LOCATION": "us-central1",
}

app = AdkApp(agent=agent)

def deploy():
    try:
        remote_agent = client.agent_engines.create(
            agent=app,
            config={
            # "source_packages":["./fun_agent"],
            "entrypoint_module":"fun_agent.agent",
            "entrypoint_object":"root_agent",
            "requirements_file":"requirements.txt",
            "display_name":"fun_agent",
            # identity_type=types.IdentityType.AGENT_IDENTITY,
            "agent_framework":"google-adk",
            }
        )
        print(f"Deployed agent: {remote_agent}")
    except Exception as e:
        print(f"Unable to deploy agent: {e}")

if __name__ == "__main__":
    deploy()

