from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage(content="You are expert doctor"),
    HumanMessage(content="tell me about diabetes in 1 line"),
]
model = ChatOpenAI()
result = model.invoke(messages)
messages.append(AIMessage(result.content))
print(messages)
