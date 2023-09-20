import datetime
from flask import (jsonify, render_template,
                   request, url_for, flash, redirect)
import json
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

    app.logger.debug(str(len(d)) + " entries in phonebook")


    return jsonify(d)  # convert your data to JSON and return

@app.route('/test')
def resume():
    return app.send_static_file('test.html')

@app.route('/test_render_template')
def test_home():
    return render_template('test_render_template/index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/test_render_template/about/')
def test_about():
    return render_template('test_render_template/about.html')

@app.route('/test_render_template/comments/')
def test_comments():
    raw_json = read_file('data/messages.json')
    messages = json.loads(raw_json)
    return render_template('test_render_template/comments.html', comments=messages)

def read_file(filename, mode="rt"):
    with open(filename, mode, encoding='utf-8') as fin:
        return fin.read()




def write_file(filename, contents, mode="wt"):
    with open(filename, mode, encoding="utf-8") as fout:
        fout.write(contents)

@app.route('/test_render_template/create/', methods=('GET', 'POST'))
def test_create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']


        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            raw_json = read_file('data/messages.json')
            messages = json.loads(raw_json)
            messages.append({'title': title, 'content': content})
            write_file('data/messages.json', json.dumps(messages, indent=4))
            return redirect(url_for('test_comments'))
        
    return render_template('test_render_template/create.html')