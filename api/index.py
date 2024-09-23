from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'PLEASE PLEASE PLEASE BRUHRHRHR'

@app.route('/about')
def about():
    return 'About'
