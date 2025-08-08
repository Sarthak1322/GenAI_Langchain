from langchain.llms import OpenAI 
from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate

llm = OpenAI(model_name="gbt-3.5-turbo", temperature=0.7)

prompt = PromptTemplate(
    template="Suggest a cacty blog title about {topic}",
    input_variables=["topic"]
)

chain = LLMChain(llm=llm, prompt=prompt)

topic = input("Enter a topic")
output = chain.run(topic)

print("Generate Blog Title", output)

