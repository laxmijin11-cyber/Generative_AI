from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a hepful customer suppert agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ]
)

chat_history = []

# load chat history
with open("chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke(
    {"chat_history": chat_history, "query": "tell me about refund"}
)
# chat template mai hum dictionary de rahe hai
print(prompt)
# Error 1: chat_history.append(f.readlines()) — This appends a list inside a list. So chat_history becomes [[line1, line2, ...]] instead of [line1, line2, ...].

# Error 2: You're passing plain strings into MessagesPlaceholder,
# but it expects message objects (HumanMessage, AIMessage).But we have specified it as HumanMesaage before itself
