from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import ChatPromptTemplate

# from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

# chat_template=ChatPromptTemplate.from_messages() also works!
chat_template = ChatPromptTemplate(
    [
        # SystemMessage(content='You are {domain} expert'),
        # HumanMessage(Content='Explaon about {topic}')
        # Using tuples
        ("system", "You are {domain} expert"),
        ("human", "Explaon about {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "Doctor", "topic": "Diabetes"})

print(prompt)
