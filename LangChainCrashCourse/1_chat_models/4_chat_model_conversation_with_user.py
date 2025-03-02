from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Conversation with LLM through terminal (similar to how inside chatGPT application works)
# remembers the chat history and uses it to generate the next response.

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

chat_history = []  # Use a list to store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    # print("Chat history before we invoke: ", chat_history) # [SystemMessage(content='You are a helpful AI assistant.', additional_kwargs={}, response_metadata={}), HumanMessage(content='What is the square root of 49', additional_kwargs={}, response_metadata={})]

    # Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add AI message

    print(f"AI: {response}")

print("---- Message History ----")
print(chat_history)
