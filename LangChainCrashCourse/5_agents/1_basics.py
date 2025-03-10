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
# result = chain.invoke({"input": query}) # query we providing this as an input to the chain, so line 17 gets converted into a prompt and gets sent to the LLM.
# print(result) # I'm sorry, but I am not able to provide real-time information as I do not have the capability to access current time data. Please check your phone, computer, or other electronic device for the current time.
# LLMs by itself cannot access real time data, they are trained on some data and usually have a cut-off date as well but if I ask it something that happened today morning chances are it does not know.
# This is a perfect example where we can give more ability to LLM by creating agent. Now that agent can use a tool to figure out the current time.


@tool # this is a decorator that tells the agent that this function is a tool and changes this method into the format that LangChain can easily understand
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """ # this is a docstring that tells the agent what this tool does, so beacuse of this llm will know if it should use this tool or not for a particular task.

    current_time = datetime.datetime.now() # gives us current system date and time (import datetime)
    formatted_time = current_time.strftime(format)
    return formatted_time

llm = ChatOpenAI(model="gpt-4o-mini")

query = "What is the current time in London? (You are in India). Just show the current time and not the date"

prompt_template = hub.pull("hwchase17/react") # react prompt we are pulling from langchain hub.
# https://smith.langchain.com/hub/hwchase17/react

tools = [get_system_time] # tools is a list, We can provide lot of tools to the agent, and depending on what the agent is solving at that particular point of time it can use the right tool to get the job done.

agent = create_react_agent(llm, tools, prompt_template) # 2:20:00

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)# verbose = True because we want to be able to see what the agent is thinking and what it is doing at every step of the way (use it as logs to debug)

agent_executor.invoke({"input": query})

