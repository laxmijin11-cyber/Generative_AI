from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model="claude-3-5-haiku-20241022", max_tokens=12)

response = model.invoke("What is capital of India?")

print(response.content)
