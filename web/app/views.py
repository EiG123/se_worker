from flask import jsonify
import json
import os
from app import app

@app.route('/')
def home():
    return "Bank says: 'Hello World!'"

@app.route('/db/')
def db_connection():
    # Define the path to check.student.json
    json_file_path = os.path.join(app.root_path, 'model', 'check.student.json')

    # Read the JSON data from check.student.json
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Pretty-print the JSON for better readability
        formatted_data = json.dumps(data, indent=4)

        return "<pre>{}</pre>".format(formatted_data)
    except FileNotFoundError:
        return f'<h1>JSON file not found at {json_file_path}</h1>'
