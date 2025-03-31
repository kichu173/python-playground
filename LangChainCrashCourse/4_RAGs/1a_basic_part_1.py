# Implementing the first part of the RAG.png image, 1a, 1b
# Here we are using chromadb as our vector db/store. So embeddings are stored locally in the db directory and not in the cloud.
# Lord of the Rings book is used as the document to be embedded and stored in the db directory.

import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Define the directory containing the text file and the persistent directory (load the document)
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "documents", "lord_of_the_rings.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db") # embeddings are stored locally in the db directory and not in the cloud.

# Check if the Chroma vector store already exists (text to embeddings cost little bit of money, so we are making this check to avoid re-embedding the text file)
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # Read the text content from the file
    loader = TextLoader(file_path) # to load the document/book in memory.
    documents = loader.load()

    # Split the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50) # chunk_size=1000 - include 1000 characters, chunk_overlap - If you are working with complex texts like essays /novels, it's better to give somewhere b/n 50-100 characters. If you are working with simple text you can leave it with 0.
    docs = text_splitter.split_documents(documents) # array of chunks of text.

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Create embeddings
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )  # Update to a valid embedding model if needed (text-embedding-3-large)
    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it automatically
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating vector store ---")

else:
    print("Vector store already exists. No need to initialize.")




# Questions to ask
# Who is the Ring-bearer?
# Where does Gandalf meet Frodo?