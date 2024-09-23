from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'PLEASE PLEASE PLEASE DONT PROVE IM RIGHTTTTTTT'

@app.route('/about')
def about():
    return 'About'
