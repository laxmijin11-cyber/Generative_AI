# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=75,
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate a small report on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate a 5 pointer summary from the following text \n {text}",
    input_variables=["text"],
)

# model = ChatOpenAI()
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "unemployment"})

print(result)

chain.get_graph().print_ascii()
# pip install grandalf
