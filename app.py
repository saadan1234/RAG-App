from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.vectorstores.chroma import Chroma


#Content base path 
data_path = 'content_base'

#Loads pdf documents. 
#For other types of docs, check document loaders on langchain.
def load_documents():
    document_loader = PyPDFDirectoryLoader(data_path)
    return document_loader.load()

#Breaking text into seperate chunks for quering
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 80,
        length_function = len,
        is_separator_regex= False
    )
    return text_splitter.split_documents(documents)

#Embedding Functions using locally run Ollama server
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="llama3")
    return embeddings

#Chroma Vector Database
def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )
    db.add_documents(new_chunks, ids= new_chunk_ids)
    db.persist

#Testing load_documents() function
# documents = load_documents()
# chunks = split_documents(documents)
# print(chunks[0])



