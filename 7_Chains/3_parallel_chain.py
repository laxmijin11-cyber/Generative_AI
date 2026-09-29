from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=75,
)
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"],
)
prompt2 = PromptTemplate(
    template="Generate 5 short ques and ans from the following text \n {text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="Merge the notes and ques and ans into single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()
parallel_chain = RunnableParallel(
    {"notes": prompt1 | model | parser, "quiz": prompt2 | model | parser}
)

merge_chain = prompt3 | model | parser
chain = parallel_chain | merge_chain
text = """
elephant is intelligent.
"""

result = chain.invoke({"text": text})
print(result)

chain.get_graph().print_ascii()
