from langchain_community.embeddings.ollama import OllamaEmbeddings

#Embedding Functions using locally run Ollama server
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    return embeddings