from app import app


@app.route('/')
def home():
    return "Bank says :'Hello World!'"