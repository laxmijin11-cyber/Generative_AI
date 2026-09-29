import random

from abc import ABC, abstractmethod


class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass


class NakliLLM(Runnable):
    def _init_(self):
        print("LLM created")

    def invoke(self, prompt):
        response_list = [
            "Delhi is the capital of india",
            "IPL is cricket league",
            "AI stands for Artificial Inteliigence",
        ]

        return {"response": random.choice(response_list)}

    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of india",
            "IPL is cricket league",
            "AI stands for Artificial Inteliigence",
        ]

        return {"response": random.choice(response_list)}

    # dont remove predict show warning fro deprecated


llm = NakliLLM()

result = llm.predict("What is capital of India")
# print(result)


class NakliPromptTemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)


template = NakliPromptTemplate(
    template="Write a {length} poem about {topic}", input_variables=["topic", "length"]
)
print(template.format({"topic": "India", "length": "short"}))
prompt = template.format({"topic": "India", "length": "short"})
llm = NakliLLM()
result = llm.predict(prompt)
# print(result)


class NakliLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result["response"]


template = NakliPromptTemplate(
    template="write {length} poem on {topic}", input_variables=["length", "topic"]
)

llm = NakliLLM()
chain = NakliLLMChain(llm, template)

result = chain.run({"length": "short", "topic": "india"})
# print(result)


class NakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data["response"]


class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data


template = NakliPromptTemplate(
    template="write {length} poem on {topic}", input_variables=["length", "topic"]
)
llm = NakliLLM()

parser = NakliStrOutputParser()

chain = RunnableConnector([template, llm, parser])
print(chain.invoke({"length": "long", "topic": "India"}))


# CONNECTING THE RUNNABLES
template1 = NakliPromptTemplate(
    template="write a joke on {topic}", input_variables=["topic"]
)

template2 = NakliPromptTemplate(
    template="Explain the following joke {response}", input_variables=["response"]
)
llm = NakliLLM()
parser = NakliStrOutputParser()

chain1 = RunnableConnector([template1, llm])
chain1.invoke({"topic": "Love"})
chain2 = RunnableConnector([template2, llm, parser])
chain2.invoke({"response": "This is a joke"})

final_chain = RunnableConnector([chain1, chain2])
print(final_chain.invoke({"topic": "cricket"}))


# standardize karna hoga classes ko-invoke() like common functions
# Abstraction:jitne components h sabme same methods ho
# making abstract class runnableand baaki sari class uss runnable class se inherit karegi-common structure-abstract methodsABC:ABSTRACT BASE CLASSES
