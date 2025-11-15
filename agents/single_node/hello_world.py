# Import following modules
from typing import Dict, TypedDict, Any
from langgraph.graph import StateGraph

# Define agent state class
class AgentState(TypedDict):
    message: str
    
# Define basic node
def greeting_node(state: AgentState) -> AgentState:
    """ Simple node that adds a greeting message to the state

    Args:
        state (AgentState): Shared data structure that maintains the state of the program

    Returns:
        AgentState: Updated agent state
    """
    state['message'] = "Hello " + state["message"]
    return state

# Set up graph structure
graph: StateGraph = StateGraph(AgentState)

# Add greeter node to graph
graph.add_node("greeter", greeting_node)

# Connect entry and exit points of the graph to the greeter node
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result: dict[str, str | Any] = app.invoke({"message": "Bob"})

print(result)