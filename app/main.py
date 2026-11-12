from app.document_loader import load_document 
from app.chunker import split_text 
from app.embeddings import create_embeddings 
from app.storage import store_chunks 

#load documents 

documents = load_document() 

#split documents into chunks 

chunks = split_text(documents) 

#generate embeddings 

vectors = create_embeddings(chunks) 

#store embeddings and chunks in PostgreSQL 

store_chunks(chunks, vectors) 

print("Document processing completed")