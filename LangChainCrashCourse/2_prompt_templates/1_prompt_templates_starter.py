from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

# Step1 - we create a string with placeholders, this string is only a prompt that you and I can understand.
template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

# Step2 - convert the string into a template that the system(LangChain) can understand
# prompt_template = ChatPromptTemplate.from_template(template)
#
# print(prompt_template)
#
# # Step3: Invoke the template with the values for the placeholders
# prompt =  prompt_template.invoke({
#     "tone": "energetic",
#     "company": "samsung",
#     "position": "AI Engineer",
#     "skill": "AI"
# })
#
# print(prompt) # messages=[HumanMessage(content='Write a energetic email to samsung expressing interest in the AI Engineer position, mentioning AI as a key strength. Keep it to 4 lines max', additional_kwargs={}, response_metadata={})]
#
# # Step4: Invoke the prompt with the model
# result = llm.invoke(prompt)
#
# print(result.content)

# Example 2: Prompt with System and Human Messages (Using Tuples)
messages = [ # list of tuples, each tuple has two elements, the first element is the type of the message (system or human) and the second element is the content of the message itself
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print("\n----- Prompt with System and Human Messages (Tuple) ------------\n")
print(prompt) # messages=[SystemMessage(content='You are a comedian who tells jokes about lawyers.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me 3 jokes.', additional_kwargs={}, response_metadata={})]
result = llm.invoke(prompt)
print(result.content)