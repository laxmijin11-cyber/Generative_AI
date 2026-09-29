from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
O my Lord Krishna, in this dark era,
You created me, and guide my soul’s terra.
Show me the light on my path, I pray,
Lead me through night into the bright day.
"""
# Initialize the splitter
# splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=4)


# performs the splits
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)
