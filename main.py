import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["my name is Mohammed","My name is not Mohammed"],
    metadatas=[{"source":"name is true"},{"source":"name is false"}],
    ids=["ids1","ids2"]
)
results = collection.query(
    query_texts=['what is my name'],
    n_results=1

)
print(results)