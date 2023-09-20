import os
from flask import Flask
from pymongo import MongoClient


app = Flask(__name__, static_folder='static')

# Set your MongoDB URI
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['hello_mongo_dev']  # Replace with your MongoDB database name

app.config['SECRET_KEY'] = 'a8112ea716969327fc2a49fc8dd0e2ca9fa484033e771552'
app.config['JSON_AS_ASCII'] = False

# This ensures that Flask won't track modifications to the MongoDB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Optional: Uncomment these lines if you want to use SQLAlchemy (not needed for MongoDB)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
# db = SQLAlchemy(app)

from app import views  # noqa