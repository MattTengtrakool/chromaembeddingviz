from flask import Flask, request, jsonify
from dataservice.chroma_service import ChromaService
from flask_cors import CORS

app = Flask(__name__)

dummy_data = [
    {
        "_id": "1",
        "name": "Dummy Document 1",
        "vector": [0.1, 0.2, 0.3, 0.4, 0.5]
    },
    {
        "_id": "2",
        "name": "Dummy Document 2",
        "vector": [0.6, 0.7, 0.8, 0.9, 1.0]
    },
]

chroma_service = ChromaService('my_collection', dummy_data)

CORS(app)

@app.route('/create_collection/', methods=['POST'])
def create_collection():
    data = request.get_json()
    chroma_service.create_collection(data['name'])
    return jsonify({"message": "Collection created successfully."}), 200

@app.route('/add_documents/', methods=['POST'])
def add_documents():
    data = request.get_json()
    chroma_service.add_documents(data['documents'], data['metadatas'], data['ids'])
    return jsonify({"message": "Documents added successfully."}), 200

@app.route('/add_embeddings/', methods=['POST'])
def add_embeddings():
    data = request.get_json()
    chroma_service.add_embeddings(data['embeddings'], data['documents'], data['metadatas'], data['ids'])
    return jsonify({"message": "Embeddings added successfully."}), 200

@app.route('/query_collection/', methods=['POST'])
def query_collection():
    data = request.get_json()
    results = chroma_service.query_collection(data['query_texts'], data['n_results'])
    return jsonify(results), 200

if __name__ == "__main__":
    app.run(debug=True)
