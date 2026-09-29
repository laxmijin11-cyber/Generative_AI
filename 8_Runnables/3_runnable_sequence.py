from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=55,
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the joke in 1 line \n {text}", input_variables=["text"]
)

parser = StrOutputParser()
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
result = chain.invoke({"topic": "Love"})
print(result)


"""
The joke is a play on words, using the phrase "take their love to the next level" (meaning to elevate their relationship) literallywith a ladder, and also referencing the idea of progressing to a new level in a relationship.
"""
