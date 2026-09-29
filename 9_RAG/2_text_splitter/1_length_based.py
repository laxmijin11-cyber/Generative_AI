from langchain_text_splitters import CharacterTextSplitter

# pip install langchain-text-splitters
text = """
O my Lord Krishna, in this dark era,
You created me, and guide my soul’s terra.
Show me the light on my path, I pray,
Lead me through night into the bright day.
"""
splitter = CharacterTextSplitter(chunk_size=5, chunk_overlap=0, separator="")

result = splitter.split_text(text)
print(result)
