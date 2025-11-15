from typing import TypedDict, Any
from langgraph.graph import StateGraph

# Define agent state class
class AgentState(TypedDict):
    name: str
    
# Define node that modifies the existing state 
def compliment(state: AgentState) -> AgentState:
    """Simple node that adds a compliment to the name provided by state

    Args:
        state (AgentState): The state of the program

    Returns:
        AgentState: Updated program state
    """
    state["name"] = state["name"] + ", you're doing so well"
    return state

graph: StateGraph = StateGraph(AgentState)
graph.add_node("compliment", compliment)

graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app = graph.compile()

result: dict[str, str | Any] = app.invoke({"name": "Bob"})
print(result)