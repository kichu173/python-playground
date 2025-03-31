# Implementing the second part of the RAG.png image, 1a, 1b. User's prompt/question is also embedded in the code and send to retriever.
# we are only going to pull the most relevant chunks of information from the vector db based on the users prompt.

import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Define the embedding model (whichever embedding model that we used to embed your private data, we need to use the same model here as well to embed users question as well.)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Load the existing vector store with the embedding function - (we are loading the vector store in this case the chroma db, so the db is available to use inside this file)
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings) # embed the users prompt/question as well to search the db for the right chunks of information.

# Define the user's question
query = "Where does Gandalf meet Frodo?"

# Retrieve relevant documents based on the query (configure the retriever)
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.5}, # we're specifying just how many highest relevant chunks that we want retriever to bring. Here it is going to collect the top three chunks with the highest similarity score.
)# score_threshold goes between 0- 1 (1 represents the highest similarity score), 0.5 or higher, so it is going to collect top 3 chunks that have the similarity score of 0.5 or higher. (0.5 is a good starting point, but you can adjust it based on your needs.)

relevant_docs = retriever.invoke(query) # magic keyword - invoke() we're going to be using to take action in LangChain, also invoke here makes query embedded.

# Display the relevant results with metadata (relevant chunks that are getting generated based on the users prompt)
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")

"""
The `1` passed as the second argument to `enumerate()` sets the starting index for enumeration. By default, `enumerate()` starts counting from 0, but when you pass `1`, it will start counting from 1 instead.

In this case, when you iterate over the documents:
- Without the second argument: `enumerate(relevant_docs)` would yield pairs like `(0, doc1)`, `(1, doc2)`, `(2, doc3)`
- With `enumerate(relevant_docs, 1)`, it yields pairs like `(1, doc1)`, `(2, doc2)`, `(3, doc3)`

This is particularly useful here because it's being used to display document numbers to users in a more natural way (starting from 1 instead of 0).
"""