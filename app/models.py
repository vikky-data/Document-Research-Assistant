from sqlalchemy import Column, Integer, String, Text 
from sqlalchemy.orm import declarative_base 
from pgvector.sqlalchemy import Vector 


Base = declarative_base()

class DocumentChunk(Base): 
    __tablename__ = "document_chunk" 

    id = Column(Integer, primary_key=True, index=True)
    content  = Column(Text, nullable = False) 
    source = Column(String) 
    page_number = Column (Integer)
    embedding = Column (Vector(384)) 
