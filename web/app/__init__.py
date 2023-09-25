import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__, static_folder='static')

MONGO_URI = os.getenv('DATABASE_URL', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client.get_database()  # The default database

app.config['SECRET_KEY'] = 'a8112ea716969327fc2a49fc8dd0e2ca9fa484033e771552'
app.config['JSON_AS_ASCII'] = False

# This ensures that Flask won't track modifications to the MongoDB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import views  # noqa