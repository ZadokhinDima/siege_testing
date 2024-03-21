from flask import Flask, request, jsonify
from pymongo import MongoClient
import random
import string

app = Flask(__name__)
client = MongoClient('mongodb://admin:adminpassword@localhost:27017/')
db = client['test_data']
collection = db['test_collection']

@app.route('/save', methods=['GET'])
def save_document():
    name = ''.join(random.choices(string.ascii_letters, k=10))
    print("SAVING DOCUMENT: ", name)
    document = {'name': name}
    collection.insert_one(document)
    
    filtered_documents = collection.find({'name': {'$regex': '^' + name[:2]}})
    names = [doc['name'] for doc in filtered_documents]
    
    print("Fetched documents: ", names)

    return jsonify(names)

if __name__ == '__main__':
    app.run()