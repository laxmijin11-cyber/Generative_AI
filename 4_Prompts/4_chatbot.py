from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
chat_history = [SystemMessage(content="you are helpful assistant")]
while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content[0]["text"]))
    print("AI:", result.content[0]["text"])

print(chat_history)

# invoke can work well with list of messages and string.
# result.content is a list of dicts. You need [0] to get the first dict, then ["text"] to get the text value.
