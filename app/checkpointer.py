
from langgraph_checkpoint_cosmosdb import CosmosDBSaver

# Checkpointer backed by Azure Cosmos DB to persist agent state across sessions.
checkpointer = CosmosDBSaver(
    database_name='agent_db',
    container_name='checkpoints'
)

if __name__ == "__main__":
    user_id = "1"
    session_id = "1"
    thread_id = f"{user_id}::{session_id}"  # multi-user + multi-session isolation
    config = {"configurable": {"thread_id": thread_id}}
    print(list(checkpointer.list(config=config)))