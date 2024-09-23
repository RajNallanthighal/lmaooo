from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'PLEASE I BEG ON DIDDY'

@app.route('/about')
def about():
    return 'About'
