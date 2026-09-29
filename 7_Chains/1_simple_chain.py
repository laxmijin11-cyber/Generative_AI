# PROMPT--->llm--->RESPONSE IN  CORRECT FORMAT
# sequential chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="Generate 5 interactive facts about {topic}", input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic": "cricket"})

# prompt call- modelcall -parser ka invoke function call hoga

print(result)
chain.get_graph().print_ascii()
