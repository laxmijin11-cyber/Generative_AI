from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.chains import LLMChain

# initiate the llm
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"], template="Suggest a catchy blog title about {topic}"
)
# Define the input
# topic = input("Enter a topic:")

# Format the prompt manually
# formatted_prompt = prompt.format(topic=topic)

# call LLM directly
# blog_title = llm.predict(formatted_prompt)

# print output
# print("Generated Blog Title:", blog_title)

# Create a LLMChain
chain = LLMChain(llm=llm, prompt=prompt)
topic = input("Enter a topic:")
output = chain.run(topic)
print(output)
