from chromadb import Client

class ChromaService:
    def __init__(self, collection_name, dummy_data):
        self.chroma_client = Client()

        # Create a new collection
        self.collection = self.chroma_client.create_collection(collection_name)

        # Prepare data for the upsert function
        ids = [d['_id'] for d in dummy_data]
        embeddings = [d['vector'] for d in dummy_data]
        metadatas = [{k: v for k, v in d.items() if k not in ['_id', 'vector']} for d in dummy_data]

        # Insert dummy data into the collection
        self.collection.upsert(ids, embeddings, metadatas)

    def create_collection(self, name):
        self.collection = self.chroma_client.create_collection(name)

    def add_documents(self, documents, metadatas, ids):
        self.collection.add(documents=documents, metadatas=metadatas, ids=ids)

    def add_embeddings(self, embeddings, documents, metadatas, ids):
        self.collection.add(embeddings=embeddings, documents=documents, metadatas=metadatas, ids=ids)

    def query_collection(self, query_texts, n_results):
        return self.collection.query(query_texts=query_texts, n_results=n_results)
