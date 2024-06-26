import autogen

def main():
    config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )

    assisant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list":config_list
        }
    )


    user_proxy = autogen.UserProxyAgent(
        name="user",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )