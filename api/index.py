from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'FUCK ME ITS 9:56 ON A TUESDAY'

@app.route('/about')
def about():
    return 'About'
