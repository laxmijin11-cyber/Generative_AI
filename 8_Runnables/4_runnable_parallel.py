from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=50,
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Generate a linkedin post about {topic}", input_variables=["topic"]
)
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin": RunnableSequence(prompt2, model, parser),
    }
)

result = parallel_chain.invoke({"topic": "AI"})
print(result)
print(result["tweet"])
print(result["linkedin"])

"""
{'tweet': 'Here\'s a tweet about AI:\n\n"AI is no longer just a concept, it\'s a reality! From virtual assistants to self-driving cars, AI is transforming industries and changing the way we live and work. What\'s the most exciting AI innovation you', 'linkedin': 'Here\'s a potential LinkedIn post about AI:\n\n**Title:** "The Future is Now: How AI is Revolutionizing Industries and Changing the Game"\n\n**Post:**\n\nAs we navigate the complexities of a rapidly changingworld, one thing is clear: Artificial Intelligence growing at fast rate'}
Here's a tweet about AI:

"AI is no longer just a concept, it's a reality! From virtual assistants to self-driving cars, AI is transforming industries and changing the way we live and work. What's the most exciting AI innovation you
Here's a potential LinkedIn post about AI:

**Title:** "The Future is Now: How AI is Revolutionizing Industries and Changing the Game"

**Post:**

As we navigate the complexities of a rapidly changing world, one thing is clear: Artificial Intelligence growing at fast rate.
"""
