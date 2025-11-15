from typing import TypedDict, Any
from langgraph.graph import StateGraph, START, END

# Code to design a basic calculator using langgraph

# State maintained throughout graph
class AgentState(TypedDict):
    finalNumber: int
    operandA: int
    operandB: int
    operation: str

# Functions executed within each node
def adder(state: AgentState) -> AgentState:
    """ 
    Adds two operands from state together and stores the final number in the state 
    """
    state['finalNumber'] = state['operandA'] + state['operandB']
    return state

def subtractor(state: AgentState) -> AgentState:
    """ 
    Subtracts two operands from state together and stores the final number in the state 
    """
    state['finalNumber'] = state['operandA'] - state['operandB']
    return state

def divider(state: AgentState) -> AgentState:
    """ 
    Divides two operands from state together and stores the final number in the state 
    """
    state['finalNumber'] = state['operandA'] // state['operandB']
    return state

def multiplier(state: AgentState) -> AgentState:
    """ 
    Multiplies two operands from state together and stores the final number in the state 
    """
    state['finalNumber'] = state['operandA'] * state['operandB']
    return state

# Used with the conditional edge. Allows to decide which node we will go to based on operation
def decide_next_node(state: AgentState) -> str | None:
    """
    Determines the next node based on arithmatic operation
    """
    
    if state['operation'] == "+":
        return "add_operation"
    elif state['operation'] == "-":
        return "sub_operation"
    elif state['operation'] == "/":
        return "div_operation"
    elif state['operation'] == "*":
        return "mul_operation"
    

graph: StateGraph = StateGraph(AgentState)

# Add graph nodes
graph.add_node("add_operation", adder)
graph.add_node("sub_operation", subtractor)
graph.add_node("div_operation", divider)
graph.add_node("mul_operation", multiplier)

# Creates a node that will return the state as it is.
# This is used instead of directly connecting 'START' to the conditional edge, as the conditional edge requires the state to determine the routing, and START does not execute any function, meaning that the state is not necessarily being passed.
graph.add_node("decider", lambda state:state)
graph.add_conditional_edges(
    "decider",
    decide_next_node,
    {
        "add_operation": "add_operation",
        "sub_operation": "sub_operation",
        "mul_operation": "mul_operation",
        "div_operation": "div_operation",
    }   
)

# Add start and end to graph
graph.add_edge(START, "decider")

graph.add_edge("add_operation", END)
graph.add_edge("sub_operation", END)
graph.add_edge("mul_operation", END)
graph.add_edge("div_operation", END)

app = graph.compile()

# Example operation for 5 // 7

data = {
    "operandA": 5,
    "operandB": 7,
    "operation": "/"
}
result = app.invoke(data)
print(result)




    