from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", max_tokens=3)

result = model.invoke("what is capital of india")
print(result.content)
