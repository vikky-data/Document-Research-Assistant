from langchain_text_splitters import RecursiveCharacterTextSplitter 
from app.document_loader import load_document 

def split_text(document):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    ) 

    chunks = text_splitter.split_documents(document)

    print(len(chunks)) 

    return chunks 

loading = load_document() 
result = split_text(loading)

print(result) 

