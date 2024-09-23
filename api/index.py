from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'OOOOOOOH SHINY'

@app.route('/about')
def about():
    return 'About'
