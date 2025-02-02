import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from embedding import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# def main():
#     # Create CLI.
#     parser = argparse.ArgumentParser()
#     parser.add_argument("query_text", type=str, help="The query text.")
#     args = parser.parse_args()
#     query_text = args.query_text
#     query_rag(query_text)


def query_rag(query_text: str, model: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=3)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)
    if model == "gemma2":
        model = Ollama(model="gemma2")  
    else:
        model = Ollama(model="llama3")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_sources = []
    formatted_response = f"Response: {response_text}\n"
    for source in sources:
        parts = source.split(':')
        file_path = parts[0]
        page_number = parts[1]
        chunk_number = parts[2]
        file_name = file_path.rsplit('\\', 1)[1].rsplit('.', 1)[0]
        formatted_sources.append(f"Pdf Page: {page_number} Chunk Number: {chunk_number} Source: {file_name}\n")
    return (formatted_response, formatted_sources)


# if __name__ == "__main__":
#     main()