# https://docs.langchain.com/oss/python/integrations/document_loaders


class MyCustomLoader(BaseLoader):
    """
    Custom loader to read text files from a directory and return LangChain Document objects.
    """

    def __init__(self, directory_path: str):
        if not isinstance(directory_path, str):
            raise TypeError("directory_path must be a string.")
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")
        self.directory_path = directory_path

    def load(self):
        """
        Loads all .txt files from the directory into LangChain Document objects.
        """
        docs = []
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)

            # Only process .txt files
            if filename.lower().endswith(".txt") and os.path.isfile(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        if content:  # Skip empty files
                            docs.append(
                                Document(
                                    page_content=content, metadata={"source": file_path}
                                )
                            )
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
        return docs

    def lazy_load(self):
        """
        Generator version of load() for large datasets.
        """
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            if filename.lower().endswith(".txt") and os.path.isfile(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        if content:
                            yield Document(
                                page_content=content, metadata={"source": file_path}
                            )
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")


# Example usage
if __name__ == "__main__":
    loader = MyCustomLoader("./data")  # Directory containing .txt files
    documents = loader.load()  # Load all documents
    print(f"Loaded {len(documents)} documents.")
    for doc in documents:
        print(doc.metadata, doc.page_content[:50], "...")
# Key Points
# BaseLoader

# All custom loaders must inherit from BaseLoader.
# Implement load() (returns a list of Document objects).
# Optionally implement lazy_load() (yields documents one by one).
# Document Object

# page_content: The actual text.
# metadata: Dictionary with extra info (e.g., file path, source).
# Error Handling

# Validate inputs.
# Handle file read errors gracefully.
# Lazy Loading

# Useful for large datasets to avoid memory overload.
