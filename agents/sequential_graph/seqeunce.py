from typing import TypedDict, Any
from langgraph.graph import StateGraph

# Create agent state class that will be passed throughout the graph
class AgentState(TypedDict):
    name: str
    age: str
    final: str
    

# Function that will be executed in the first node of the graph
def node_one(state: AgentState) -> AgentState:
    """This is the first node of our sequence. It will concat a string to the 'final' key"""
    state["final"] = f"Hi {state['name']}!"
    return state

# Function that will be executed in the second node of the graph
def node_two(state: AgentState) -> AgentState:
    """This is the second node of the sequence. It will concat the state age to state final"""
    state["final"] = f"{state['final']} You are {state['age']} years old"
    return state

graph: StateGraph = StateGraph(AgentState)

# Add nodes to the graph. When adding nodes, the edges are not defined, so these two nodes are not connected
graph.add_node("one", node_one)
graph.add_node("two", node_two)

# This function adds the two nodes together. The first node is the first arguement, and the next node is the second arguement
graph.add_edge("one", "two")

graph.set_entry_point("one")
graph.set_finish_point("two")

app = graph.compile()

result: dict[str, str] = app.invoke({"name": "Katie", "age": "24", "final": ""})
print(result)