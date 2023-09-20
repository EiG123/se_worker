from flask import Flask

app = Flask(__name__, static_folder='static')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '2523871733b09fc385425612808cd5f7a6e5b05d31f094d0'

from app import views # noqa