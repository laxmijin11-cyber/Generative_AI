# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

# 1st prompt-->detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)
# 2nd prompt-summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text /n {text}",
    input_variables=["text"],
)
parser = StrOutputParser()
# entire flow:pipeline
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic": "bloack hole"})

print(result)
# parser aaya and usne result mai se string output nikala and passed to second template
