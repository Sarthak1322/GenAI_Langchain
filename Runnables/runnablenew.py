import random

from abc import ABC, abstractmethod


class Runnable(ABC):


    @abstractmethod
    def invoke(input_data):
        pass

class NakliLLM(Runnable):
    def __init__(self):
        print("LLM created")

    def invoke(self, prompt):
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return{'response': random.choice(response_list)}


    def predict(self, prompt):
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return{'response': random.choice(response_list)}
    
class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)


    def Format(self, input_dict):
        return self.template.format(**input_dict)
    
class RunnableConnector(Runnable):

    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        
     
template = NakliPromptTemplate(
    template="Write a poem about {topic}",
    input_variables=['topic']
)

llm = NakliLLM()

chain = RunnableConnector([template, llm])

chain.invoke({'topic': 'india'})

template1 = NakliPromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

template2 = NakliPromptTemplate(
    template="Explain the following joke {response}",
    input_variables=['response']
)

chain1 = RunnableConnector([template1, llm])

# chain1.invoke({'topic': 'AI'})

chain2 = RunnableConnector([template2, llm])

# chain1.invoke({'response': 'This is a joke'})

final_chain = RunnableConnector([chain1, chain2])

final_chain.invoke({'topic': 'cricket'})