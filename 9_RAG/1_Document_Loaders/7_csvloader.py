from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r"C:\users\admin\Downloads\netflix_titles.csv")

data = loader.load()

print(data[0])
print(len(data))


# can use lazy_load() a swell like genrator of objects se chala sakte ho

"""
**Yes, same rule for all loaders.**

Replace `langchain_community.document_loaders` with dedicated packages:

| Loader | New Package | Import |
|--------|-------------|--------|
| PDF | `langchain-pdf` | `from langchain_pdf import PyPDFLoader` |
| Text | `langchain-community` still works for TextLoader | `from langchain_community.document_loaders import TextLoader` |
| CSV | `langchain-community` | same |
| Web | `langchain-community` | same |
| Unstructured | `langchain-unstructured` | `from langchain_unstructured import UnstructuredLoader` |

**Reality check:** Not all loaders have standalone packages yet. Some still live in `langchain-community`.

**Practical approach:**
- **If standalone package exists** → use it
- **If not** → `langchain-community` still works (just shows warning)
- **Warning is not an error** — code still runs

**Bottom line:** Warning is safe to ignore for now. Use standalone when available, else keep `langchain-community`. Migration is gradual.
"""
# https://reference.langchain.com/python/langchain-community/document_loaders
