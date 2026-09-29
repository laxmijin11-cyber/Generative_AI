from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

loader = TextLoader("krishna.txt", encoding="utf-8")
docs = loader.load()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=25,
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="write summary for following poem in 1 line \n  {poem}",
    input_variables=["poem"],
)

parser = StrOutputParser()

chain = prompt | model | parser
chain.invoke({"poem": docs[0].page_content})
