# pip install PyPDF
from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader

# loader = PyPDFLoader("Solution_Tutorial-3.pdf")
# docs = loader.load()
# print(docs)
# print(len(docs))

"""[Document(metadata={'producer': 'macOS Version 15.6.1 (Build 24G90) Quartz PDFContext', 'creator': 'Word', 'creationdate': "D:20260210101857Z00'00'", 'title': 'Microsoft Word - Tutorial-3.docx', 'moddate': "D:20260210101857Z00'00'", 'source': 'Solution_Tutorial-3.pdf', 'total_pages': 2, 'page': 0, 'page_label': '1'}, page_content='Solu%on: \nQ. 1 \n \nQ. 2'), Document(metadata={'producer': 'macOS Version 15.6.1 (Build 24G90) Quartz PDFContext', 'creator': 'Word','creationdate': "D:20260210101857Z00'00'", 'title':'Microsoft Word - Tutorial-3.docx', 'moddate': "D:20260210101857Z00'00'", 'source': 'Solution_Tutorial-3.pdf', 'total_pages': 2, 'page': 1, 'page_label': '2'}, page_content='Q. 3 \n \nQ. 4 \n \nQ. 5')]
"""

# print(docs[0].page_content)
# print(docs[1].metadata)

# pip install unstructured
loader = UnstructuredPDFLoader("Solution_Tutorial-3.pdf")
docs = loader.load()
print(docs)
print(len(docs))
# pip install pdfminer.six
# pip install pi-heif
# https://reference.langchain.com/python/langchain-community/document_loaders/pdf
# pip install unstructured pdf2image pytesseract
