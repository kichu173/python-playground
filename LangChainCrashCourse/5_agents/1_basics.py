from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
import datetime
from langchain.agents import tool

load_dotenv()

# llm = ChatOpenAI(model="gpt-3.5-turbo")
#
# query = "What is the current time?"
#
# prompt_template = PromptTemplate.from_template("{input}")
#
# chain = prompt_template | llm | StrOutputParser()
#
# result = chain.invoke({"input": query})
# print(result) # I'm sorry, but I am not able to provide real-time information as I do not have the capability to access current time data. Please check your phone, computer, or other electronic device for the current time.

@tool # this is a decorator that tells the agent that this function is a tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now() # gives us current system date and time
    formatted_time = current_time.strftime(format)
    return formatted_time

llm = ChatOpenAI(model="gpt-3.5-turbo")

query = "What is the current time in London? (You are in India). Just show the current time and not the date"

prompt_template = hub.pull("hwchase17/react") # react prompt we are pulling from langchain hub.
# https://smith.langchain.com/hub/hwchase17/react

tools = [get_system_time]

agent = create_react_agent(llm, tools, prompt_template)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)# verbose = True because we want to be able to see what the agent is thinking and what it is doing at every step of the way (use it as logs to debug)

agent_executor.invoke({"input": query})

