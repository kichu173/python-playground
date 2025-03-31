from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(  # interface that lets us access that particular API(OpenAI's api), Chat model here is ChatOpenAI, to initialize the LLM
    model="gpt-3.5-turbo",
    temperature=0,
)
# invoke is a magic keyword if we want to make any call to LLM
result = llm.invoke("What is the square root of 49")

print(result.content)
