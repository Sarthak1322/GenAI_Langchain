from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI 
from langchain.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA 


loader = TextLoader("docs.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings)

retriever = vectorstore.as_retriever()

llm = OpenAI(model_name="gbt-3.5-turbo",temperature=0.7)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


query = "What are the key takeway from the documents"

answer = qa_chain.run(query)
print("Answer: ", answer)