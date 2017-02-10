from flask import Flask, render_template

app = Flask(__name__)


# index route
@app.route('/')
def index():
    return render_template('index.html')


# birthday route
@app.route('/birthday')
def bday():
    return '1 January 1970'


# hello route with variable name
@app.route('/greeting/<name>')
def greet(name):
    return 'Hello, {0}!'.format(name)


# sum route
@app.route(/sum/<int:a>/<int:b>')
def sum_ints(a, b):
    return "The sum of {0} and {1} is {2}.".format(a, b, a + b)

           
