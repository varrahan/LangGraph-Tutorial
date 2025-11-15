from typing import TypedDict, Any
from langgraph.graph import StateGraph

# Define agentstate class with multiple inputs
class AgentState(TypedDict):
    values: list[int]
    name: str
    result: str
    
# Function within the node that will modify all the values of the state
def process_vals(state: AgentState) -> AgentState:
    """ This function handles multiple different inputs

    Args:
        state (AgentState): The state of the agent

    Returns:
        AgentState: The updated agent state
    """
    state["result"] = f"Hi there {state["name"]}! You're summed values are {sum(state['values'])}"
    return state

graph: StateGraph = StateGraph(AgentState)

graph.add_node("processor", process_vals)

graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

input_dict: dict[str, str | list[str] | Any] = {
    "values": [1,2,3,4,5,6],
    "name": "Bob",
    "result": ""
}

result: dict[str, str | list[str]] = app.invoke(input_dict)
print(result) 

