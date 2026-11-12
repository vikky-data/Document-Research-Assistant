from langchain_huggingface import HuggingFaceEmbeddings
from app.chunker import split_text
from app.document_loader import load_document


def create_embeddings(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors
