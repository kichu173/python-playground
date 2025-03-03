# How chains works under the hood(internals of chains) - So that we can write our own custom function in place of StrOutputParser().

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
     [
        ("system", "You love facts and you tell facts about {animal}"),
        ("human", "Tell me {count} facts."),
    ]
)

# Create individual runnables (steps in the chain) - Each task in a chain is called a Runnable.
# RunnableLambda(LangChain import) is just a simple wrapper that lets us create each task as a single reusable unit.
# Each RunnableLambda takes an input does something with it - could be like filling in a prompt or calling the model and then gives us the output.
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))# Here x is the dictionary {"animal": "cat", "count": 2} which you pass in chain.invoke() function. prompt_template.format_prompt(animal="cat", count=2)
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))# Result of format_prompt is passed to invoke_model as input. x.to_messages() is a function that converts the output of format_prompt to a list of messages.
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence (equivalent to the LCEL chain)
# RunnableSequence takes only 3 parameters, first, middle(even though you have two or three or five or more it goes to the list in middle), last)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
response = chain.invoke({"animal": "cat", "count": 2})

# Output
print(response)