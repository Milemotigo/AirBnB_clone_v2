#!/usr/bin/python3i
"""
A script that starts a flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

"""Return to display "Hello HBNB!"""


@app.route('/', strict_slashes=False)
def hello():
    """funtion that returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """funtion that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello(text):
    """funtion that returns "C <text(i.e a variable)>" """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def helloPython(text="is_cool"):
    """funtion that returns "Python <text(i.e a variable)>" """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def helloNumber(n):
    """funtion that returns "n" is a number if int else an error"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
