import chainlit as cl
from app.agent import agent 
from typing import Dict, Optional
from chainlit.types import ThreadDict
from chainlit.data.sql_alchemy import SQLAlchemyDataLayer

@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user


@cl.data_layer
def get_data_layer():
    return SQLAlchemyDataLayer(conninfo="sqlite+aiosqlite:///./chainlit.db")


@cl.on_chat_start
async def on_chat_start():
    thread_id = cl.context.session.thread_id
    cl.user_session.set("thread_id", thread_id)
    await cl.Message(content="Hello! Ask me about the weather ☀️").send()


@cl.on_message
async def on_message(message: cl.Message):
    thread_id = cl.user_session.get("thread_id")
    config = {"configurable": {"thread_id": thread_id}}

    final_state = await agent.ainvoke(
        {"messages": [{"role": "user", "content": message.content}]},
        config=config,
    )
    sr = final_state["structured_response"]

    await cl.Message(
        content=f"**{sr.punny_response}**" + (f"\n\n🌤 {sr.weather_conditions}" if sr.weather_conditions else "")
    ).send()


@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    thread_id = thread["id"]
    cl.user_session.set("thread_id", thread_id)