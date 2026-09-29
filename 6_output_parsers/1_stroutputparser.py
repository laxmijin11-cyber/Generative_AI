# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     max_new_tokens=3,
# )
# model = ChatHuggingFace(llm=llm)
# 1st prompt-->detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)
# 2nd prompt-summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text /n {text}",
    input_variables=["text"],
)

prompt1 = template1.invoke({"topic": "black hole"})
# invoke and format both works!

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})

result1 = model.invoke(prompt2)
print(result1.content)
