from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'PLEASE PLEASE PLEASE IF THERES A GOD '

@app.route('/about')
def about():
    return 'About'
