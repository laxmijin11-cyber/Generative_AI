from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnableSequence,
    RunnablePassthrough,
)

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=50,
)
template1 = PromptTemplate(
    template="generate a joke about \n {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(template="Explain about {text}", input_variables=["text"])
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


passthrough = RunnablePassthrough()

# print(passthrough.invoke(2))
# print(passthrough.invoke({"nitish": "neha"}))

joke_gen_chain = RunnableSequence(template1, model, parser)
parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explaination": RunnableSequence(template2, model, parser),
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "cricket"})
print(result)

"""
{'joke': "Here's one:\n\nWhy did the cricketer bring a ladder to the game?\n\nBecause he wanted to take his batting to the next level! (get it?)", 'explaination': 'That\'s a clever play on words. It\'s a classic example of a "pun" - a wordplay that exploits multiple meanings of a word or phrase. In this case, the phrase "take it to the next level" is a common idiom'}
"""
