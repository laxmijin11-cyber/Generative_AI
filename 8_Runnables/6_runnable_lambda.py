from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
from langchain_core.runnables import (
    RunnableParallel,
    RunnableSequence,
    RunnableLambda,
    RunnablePassthrough,
)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=35,
)


def word_counter(text):
    return len(text.split())


model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate a joke about {topic}", input_variables=["topic"]
)
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        # 'word_count':RunnableLambda(word_count)
        "word_count": RunnableLambda(lambda x: len(x.split())),
    }
)


final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

final_result = """ {} \n word count - {}""".format(result["joke"], result["word_count"])
print(final_result)


# def word_counter(text):
#     return len(text.split())


# runnable_wordcounter = RunnableLambda(word_counter)
# print(runnable_wordcounter.invoke("Hi there! how are you?"))

# In Python, the split() method splits a string into a list of substrings
# text = "apple,banana,cherry"
# result = text.split(",")  # ['apple', 'banana', 'cherry']

"""
 Why did the AI program go on a diet?

Because it wanted to lose some bytes! (get it? bytes... like computer bytes... ahh) 
word count - 23
"""
