#!/usr/bin/python3
''' a script that starts a Flask web application '''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    ''' route / to hbnb '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''route hbnb to HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints a Message when /c is called """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """ Prints a Message when /python is called """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """prints n is a number if it is an integer"""
    return f"{n} is a number"


if __name__ == '__main__':
    '''main function '''
    app.run(host='0.0.0.0', port=5000)
