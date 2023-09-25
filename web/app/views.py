from flask import jsonify, request
from app import app, db

def get_mongo_db():
    return db

@app.route('/')
def home():
    return "Bank says: 'Hello World!'"

@app.route('/db')
def db_connection():
    try:
        db.client.admin.command('ping')  # This will check the connection
        return '<h1>Database connection is complete.</h1>'
    except Exception as e:
        return '<h1>Database connection is broken.</h1>' + str(e)
if __name__ == '__main__':
    app.run()