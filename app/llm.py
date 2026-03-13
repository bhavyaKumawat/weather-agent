import os
from langchain_openai import AzureChatOpenAI


def get_llm() -> AzureChatOpenAI:
    """
    Return an AzureChatOpenAI client.

    """
    return AzureChatOpenAI(
        model=os.environ["AZURE_OPENAI_CHAT_MODEL_NAME"],
        azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"]
    )
