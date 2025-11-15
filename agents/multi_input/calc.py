from typing import TypedDict, Any
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    values: list[int]
    operation: str
    result: str

def calculate(state: AgentState) -> AgentState:
    """
    If the operation provided is *, we find the product of the values in the state, and if the operation is +, we find the sum of the values in the state. Any other operation is invalid
    """
    result: int
    if state['operation'] == "*":
        result = 1
        for value in state['values']:
            result *= value
    elif state['operation'] == "+":
        result = 0
        for value in state['values']:
            result += value
    else:
        state["result"] = f"Sorry {state['name']}, invalid operation"
        return state
    
    state["result"] = f"Hi {state['name']}, your answer is {result}"
    return state

graph: StateGraph = StateGraph(AgentState)

graph.add_node("calc", calculate)
graph.set_entry_point("calc")
graph.set_finish_point("calc")

app = graph.compile()

result: dict[str, str | list[int]] = app.invoke({"name": "Jack", "values": [1,2,3,4], "operation": "-", "result": "" })
print(result)

app = graph.compile()

result = app.invoke({})