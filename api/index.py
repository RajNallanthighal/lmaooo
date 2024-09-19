from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Howdy, Main!
    WOAH! THIS IS NEW!'

@app.route('/about')
def about():
    return 'About'
