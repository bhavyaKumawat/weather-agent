from langchain.agents import create_agent
from .llm import get_llm
from .tools.weather_tool import tools
from .checkpointer import checkpointer
from .prompts.system_prompt import SYSTEM_PROMPT
from dataclasses import dataclass


@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None


agent = create_agent(model=get_llm(), 
                     tools=tools,
                     checkpointer=checkpointer,
                     system_prompt=SYSTEM_PROMPT,
                     response_format=ResponseFormat)


if __name__ == "__main__":
    user_id = "1"
    session_id = "1"
    thread_id = f"{user_id}::{session_id}"  # multi-user + multi-session isolation
    config = {"configurable": {"thread_id": thread_id}}
    result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in my city?"}]},
        config=config
) 
    print(result["structured_response"])