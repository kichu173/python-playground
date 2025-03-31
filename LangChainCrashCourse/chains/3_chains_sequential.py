from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define prompt templates
animal_facts_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You like telling facts and you tell facts about {animal}."),
        ("human", "Tell me {count} facts."),
    ]
)

# Define a prompt template for translation to French
translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)

# Define additional processing steps using RunnableLambda
# Prompt template always requires an object that needs to be passed into it.
prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "french"})


# Create the combined chain using LangChain Expression Language (LCEL)
chain = animal_facts_template | model | StrOutputParser() | prepare_for_translation | translation_template | model | StrOutputParser()

# Run the chain
result = chain.invoke({"animal": "Lion", "count": 2})

# Output
print(result)

"""
English:
Lions are the only big cats that live in groups, known as prides. These prides typically consist of a few related adult females, their offspring, and a small number of adult males.
A lion's roar can be heard up to five miles away, making it one of the loudest animal calls in the world. This powerful roar serves to establish territory and communicate with other lions.
"""