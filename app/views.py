from flask import jsonify
from app import app


@app.route('/')
def home():
    return "Bank says :'Hello World!'"

@app.route('/phonebook')
def index():
    return app.send_static_file('phonebook.html')

# This route serves the dictionary d at the route /date
@app.route("/api/data")
def data():
    # define some data
    d = {
        "Alice": "(708) 727-2377",
        "Bob": "(305) 734-0429"
    }
    return jsonify(d)  # convert your data to JSON and return
