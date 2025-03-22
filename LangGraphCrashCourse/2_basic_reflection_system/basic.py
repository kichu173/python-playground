from typing import List, Sequence # type checking for python
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generation_chain, reflection_chain

load_dotenv()

# constants
REFLECT = "reflect"
GENERATE = "generate"
# invoke the MessageGraph class
graph = MessageGraph()

def generate_node(state):
    return generation_chain.invoke({
        "messages": state
    })


def reflect_node(state):
    response = reflection_chain.invoke({
        "messages": state
    })
    return [HumanMessage(content=response.content)] # tricking the system that reflection is done by human


graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)
graph.set_entry_point(GENERATE)


def should_continue(state):
    if (len(state) > 6):
        return END
    return REFLECT


graph.add_conditional_edges(GENERATE, should_continue)
graph.add_edge(REFLECT, GENERATE)

app = graph.compile()

# pip install grandalf
print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()

response = app.invoke(HumanMessage(content="AI Agents taking over content creation"))

print(response) # https://smith.langchain.com/
