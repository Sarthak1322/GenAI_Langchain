from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI 
from langchain.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("docs.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings)

retriever = vectorstore.as_retriever()

query = "What are the key takeway from the documents"
retriever_docs = retriever.get_relevant_documents(query)

retrieved_text = "\n".join([doc.page_content for doc in retriever_docs])

llm = OpenAI(model_name="gbt-3.5-turbo",temperature=0.7)

prompt = f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer = llm.predict(prompt)

print("Answer: ", answer)