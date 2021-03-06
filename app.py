from flask import Flask, render_template, jsonify

app = Flask(__name__)


# index route
@app.route('/')
def index():
    return render_template('index.html')


# birthday route
@app.route('/birthday/')
def bday():
    return '1 January 1970'


# hello route with variable name
@app.route('/greeting/<name>/')
def greet(name):
    return 'Hello, {0}!'.format(name)


# sum route
@app.route('/sum/<int:a>/<int:b>/')
def sum_ints(a, b):
    return "The sum of {0} and {1} is {2}.".format(a, b, a + b)


# multiply route
@app.route('/multiply/<int:a>/<int:b>/')
def multiply(a, b):
    return "{0} mulitplied by {1} is {2}.".format(a, b, a * b)


# subtract route
@app.route('/subtract/<int:a>/<int:b>/')
def subtract(a, b):
    return "{0} minus {1} is {2}.".format(a, b, a - b)


# favourite foods route
@app.route('/favoritefoods/')
def fav_foods():
    foods = ['cheese', 'bacon', 'apples', 'bread', 'more cheese']
    return jsonify(foods)
