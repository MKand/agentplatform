import vertexai
from fun_agent.agent import root_agent
import os 

project=os.getenv("GOOGLE_CLOUD_PROJECT")
client = vertexai.Client(
  project=os.getenv("GOOGLE_CLOUD_PROJECT"),
  location='us-central1',
)   

# make sure this bucket is present
bucket_name = f"gs://${project}-ae-staging-bucket"

# https://docs.cloud.google.com/agent-builder/agent-engine/deploy
remote_agent = client.agent_engines.create(
    agent=root_agent,                                  
    config={
        "requirements": ["google-adk[a2a]==1.18.0","google-cloud-modelarmor","google-cloud-aiplatform>=1.55.0"],                   
        "staging_bucket": bucket_name,   
        "gcs_dir_name": "challenge3" ,               
        "display_name": "Fun agent",                                                              
        "agent_framework": "google-adk",  
        "extra_packages": ["fun_agent"]          
    },
)
