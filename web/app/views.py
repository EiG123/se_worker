from flask import (jsonify, render_template,
                   request, url_for, flash, redirect)
import json
from sqlalchemy.sql import text
from app import app
from app import db


@app.route('/')
def home():
    return "Bank says :'Hello World!'"

@app.route('/db')
def db_connection():
    try:
        with db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return '<h1>db works.</h1>'
    except Exception as e:
        return '<h1>db is broken.</h1>' + str(e)

