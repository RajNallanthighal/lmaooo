from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'FUCK ME ITS 6:14'

@app.route('/about')
def about():
    return 'About'
