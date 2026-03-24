import vertexai

client = vertexai.Client(  # For service interactions via client.agent_engines
    project=settings.PROJECT_ID,
    location=settings.LOCATION,
)

remote_agent = client.agent_engines.create(
    config={
        "source_packages": ["./agent"],             # Required.
        "entrypoint_module": "fun_agent",         # Required.
        "entrypoint_object": "root_agent",         # Required.
        "class_methods": [],                 # Required.
        "requirements_file": "requirements.txt",         # Optional.
        "display_name": "fun_agent",                   # Optional.
        "env_vars": env_vars,                           # Optional.
        "build_options": build_options,                 # Optional.
        "identity_type": identity_type,                 # Optional.
        "service_account": service_account,             # Optional.
        "min_instances": min_instances,                 # Optional.
        "max_instances": max_instances,                 # Optional.
        "resource_limits": resource_limits,             # Optional.
        "container_concurrency": container_concurrency, # Optional
        "encryption_spec": encryption_spec,             # Optional.
        "agent_framework": agent_framework,             # Optional.
    },
)