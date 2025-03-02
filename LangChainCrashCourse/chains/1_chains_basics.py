from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
# Pipe operator is going to connect different tasks together, and once this particular task(prompt_template) is done, we pass the result to the next task which is model(llm).
# StrOutputParser is going to extract the content property alone from the whole object.
chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model

# Run the chain (Whatever we pass in here it will be available across the chain)
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Output
print(result)