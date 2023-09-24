from flask import (jsonify,render_template)
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
    
@app.route('/login')
def login():
    return render_template('inout/login.html')

@app.route('/signup')
def signup():
    return render_template('inout/register.html')

@app.route('/home')
def homepage():
    return app.send_static_file('home.html')

@app.route('/overview')
def overview():
    return app.send_static_file('overview.html')

@app.route('/teacher_home')
def t_home():
    return app.send_static_file('t_home.html')

@app.route('/subject_credit')
def s_credit():
    return app.send_static_file('sj_credit.html')

@app.route('/subject_add')
def s_add():
    return app.send_static_file('subject_add.html')

