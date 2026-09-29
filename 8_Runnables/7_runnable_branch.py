from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnableLambda,
    RunnableBranch,
    RunnablePassthrough,
)
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=20,
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="write a detailed report on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=["text"],
)
parser = StrOutputParser()

report_generation_chain = RunnableSequence(prompt1, model, parser)
# LCEL
# report_generation_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough(),
)

final_chain = RunnableSequence(report_generation_chain, branch_chain)
print(final_chain.invoke({"topic": "Russia vs Ukraine"}))

"""
Russia's ongoing invasion of Ukraine has led to significant human suffering, infrastructure destruction, and a humanitarian crisis.
"""
