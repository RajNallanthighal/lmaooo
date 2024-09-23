from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'LMAO, THIS THE DEV, LMAO, OOOOOOOH SHINY'

@app.route('/about')
def about():
    return 'About'
