from pathlib import Path 
from sqlalchemy.orm  import sessionmaker 
from app.database import engine 
from app.models import DocumentChunk 


SessionLocal = sessionmaker(bind=engine) 

def store_chunks(chunks, vectors):

    if len(chunks) != len(vectors):
        raise ValueError("The number of chunks and embeddings" \
        "must match.")

    with SessionLocal() as session:

        for chunk, vector in zip(chunks, vectors):

            document = DocumentChunk(
                content = chunk.page_content,
                source = Path(chunk.metadata["source"]).name,
                page_number = chunk.metadata.get("page",0)+ 1, 
                embedding = vector 
            ) 
            session.add(document)

            session.commit() 
print("Document chunks and embeddings saved successfully")