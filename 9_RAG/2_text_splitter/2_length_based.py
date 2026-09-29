from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader(r"C:\Users\Admin\Downloads\Laxmi_jindal_Resume_2.pdf")

docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator=" ")
result = splitter.split_documents(docs)

# print(result)

# second chunk
print(result[1].page_content)
print(docs[0].page_loader)
