import os
import getpass
import asyncio

# Setup environment


if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# Imports
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings


### INDEXING FUNCTION ###
async def build_vectorstore_from_url(url: str):
    # Load documents
    loader = WebBaseLoader(web_paths=[url])
    docs = []
    async for doc in loader.alazy_load():
        docs.append(doc)

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    # Embed
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    
    return vectorstore, docs, splits


### MAIN EXECUTION ###
async def main():
    page_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    vectorstore, docs, splits = await build_vectorstore_from_url(page_url)

    print(f"Loaded {len(docs)} raw documents.")
    print(f"Split into {len(splits)} chunks.")

    # Retriever
    retriever = vectorstore.as_retriever()

    # Prompt
    prompt = hub.pull("rlm/rag-prompt")

    # LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # Post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # Test questions
    print("\nQ1: What are the Risks and Harms of AI?")
    print(rag_chain.invoke("What are the Risks and Harms of AI?"))

    print("\nQ2: Goal of AI?")
    print(rag_chain.invoke("Goal of AI?"))

# Run the main async function
asyncio.run(main())
