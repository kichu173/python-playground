# How chains works under the hood(internals of chains) without the pipe operator - So that we can write our own custom function in place of StrOutputParser().

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

"""
The `prompt_template.format_prompt` method is necessary and serves an important purpose in this LangChain workflow:

1. **What it does:**
   - It takes your input variables (like `"cat"` and `2`) and inserts them into your prompt template
   - It replaces the placeholders `{animal}` and `{count}` with actual values

2. **Why it's necessary:**
   - It doesn't just return a regular string - it returns a special `PromptValue` object
   - This object has the `to_messages()` method that's used in the next step (`x.to_messages()`)
   - The model expects messages in a specific format, not just raw text

3. **Simpler explanation:**
   - Think of it like preparing ingredients before cooking:
     - You have a recipe (prompt template) with placeholders
     - `format_prompt` fills in those placeholders with your ingredients
     - But instead of just giving you text, it packages everything in a format that the AI model can understand

Without `format_prompt`, you'd need to manually format the prompt and convert it to the proper message structure that ChatOpenAI models expect.
"""