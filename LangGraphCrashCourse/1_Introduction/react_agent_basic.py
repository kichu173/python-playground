from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool # initialize_agent method that LangChain provides that lets you create an agent very quickly.
from langchain_community.tools import TavilySearchResults # langchain community package there are pre-built tools that we can easily use.
import datetime

load_dotenv()

# https://python.langchain.com/docs/integrations/chat/azure_chat_openai/
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_API_DEPLOYMENT_ID"),
    api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_API_ENDPOINT"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    temperature=0,
)

# for quick testing (llm works when we invoke?)
# result = llm.invoke("Give me 5 facts about guava fruit")
# print(result.content)

# LLM are just brains. They don't have any tools to interact with the external world(make search on internet, hit api's,..). So we need to give them tools to interact with the external world.

# https://app.tavily.com/home (makes a google search)
search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search_tool, get_system_time]

# zero-shot-react-description - it basically means that you're prompting the agent, the agent is doing something without any prior knowledge.
# You're not actually giving it examples or anything it is doing it based on its own reasoning ability from the scratch.
agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

agent.invoke("When was SpaceX's last launch, what was its name, and how many days ago was it from today?")

"""
C:\Users\kk000000\Documents\python-playground\LangGraphCrashCourse\1_Introduction\react_agent_basic.py:41: LangChainDeprecationWarning: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the `LangGraph documentation <https://langchain-ai.github.io/langgraph/>`_ as well as guides for `Migrating from AgentExecutor <https://python.langchain.com/docs/how_to/migrate_agent/>`_ and LangGraph's `Pre-built ReAct agent <https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/>`_.
  agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)
"""
