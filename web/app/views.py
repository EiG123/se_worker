from flask import jsonify
from app import app
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://username:password@localhost:27017/')
db = client['hello_mongo_dev']  # Replace with your MongoDB database name

@app.route('/')
def home():
    return "Bank says: 'Hello World!'"

@app.route('/db/')
def db_connection():
    try:
        # Test if MongoDB is working by listing the collections in the database
        collections = db.list_collection_names()
        return f'<h1>Connected to MongoDB. Collections: {collections}</h1>'
    except Exception as e:
        return f'<h1>Failed to connect to MongoDB. Error: {str(e)}</h1>'
