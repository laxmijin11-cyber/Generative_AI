from langchain_openai import OpenAI

# ctrl+click on OpenAI:BaseopenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-5.5")

# communicate with model by invoke method
result = llm.invoke("What is national capital of India")

print(result.content)

# string-->llm model-->string
