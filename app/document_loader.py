from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader  
from pathlib import Path 
 

#loader = PyPDFLoader("documents/01-Getting Started.pdf")
#pages = loader.load()
# print(len(pages)) 
# print(pages[0].page_content) 

def load_document():
    loader = DirectoryLoader(
        path = "documents/",
        glob = "*.pdf",
        loader_cls = PyPDFLoader
    ) 

    document = loader.load()

    print(len(document))  

    print(document[0].metadata) 

    return document 


result = load_document() 

print (result)