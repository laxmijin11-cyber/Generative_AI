from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=50,
)
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me name,age and city of fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# template = PromptTemplate(
#     template="Give me facts about {topic} \n {format_instruction}",
#     input_variables=["topic"],
#     partial_variables={"format_instruction": parser.get_format_instructions()},
# )
# chain = template | model | parser
# result = chain.invoke({"topic": "black hole"})
# print(result)
# JSON doesnot enforce schema

# json,pydantic,structuredoutputparser are some in which we send format instructions ki aapko kis tarah ka output chahiye llm se and ye baat llm ko parser baatata h by get_format_instructions is called and partial variable is bcoz it is not getting filled in runtime and isfilled before only

# prompt = template.format()
# its static prompt here
# print(prompt)

# result = model.invoke(prompt)
# print(result)
# final_result = parser.parse(result.content)

# print(final_result)
# print(final_result["name"])
# print(type(final_result))
# json objects as dict in python

chain = template | model | parser
result = chain.invoke({})
print(result)
# send blank dictionery or some dictionary to chain

# JSONOutputParser does not enforce schema
# {'name': 'Astrid Jensen', 'age': 32, 'city': 'Portland'}
