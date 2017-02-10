from flask import Flask

app = Flask(__name__)


# index route
@app.route('/')
def index():
    return 'Hello World'


# birthday route
@app.route('/birthday')
def bday():
    return '1 January 1970'


# hello route with variable name
@app.route('/greeting/<name>')
def greet(name):
    return 'Hello, {0}!'.format(name)

