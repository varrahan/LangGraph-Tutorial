from typing import TypedDict
import random
from langgraph.graph import StateGraph, START, END

# Define state that is shared among the graph
class AgentState(TypedDict):
    name: str
    number: list[int]
    counter: int

# Node that initializes counter and modifies name in state  
def greeting(state: AgentState) -> AgentState:
    """
    Greeting node to say hi to the state name
    """
    state['name'] = f"Hi {state['name']}, how are you?"
    state['counter'] = 0
    return state

# Node that updates state counter and adds random int to state number list
def random_node(state: AgentState) -> AgentState:
    """
    Generate random value and store in number list
    """
    state["number"].append(random.randint(0, 10))
    state["counter"] += 1
    print(f"{state['counter']}\n")
    return state

# Function that will be used to determine the conditional branching and loop logic
# If the counter in the state is less that 5, the graph should loop, and when counter hits 5, it will end
def should_continue(state: AgentState) -> str:
    """
    Decide whether to continue the loop or end
    """
    if state["counter"] < 5:
        return "loop"

    return "exit"


graph: StateGraph = StateGraph(AgentState)

graph.add_node("greet", greeting)
graph.add_node("random", random_node)
graph.add_edge("greet", "random")
graph.add_edge(START, "greet")

# Creates a conditional branch with two possibilities based on the return of the should_continue function.
# If the function returns loop, we see that the conditional edge is set to go back to the random node, and if the function returns exit, we end the langgraph
graph.add_conditional_edges(
    "random",
    should_continue,
    {
        "loop": "random",
        "exit": END
    }
)
 
app = graph.compile()

result = app.invoke({"name": "bagi", "number": [], "counter": 0})    
   