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


@app.route("/c/<text>", strict_slashes=False)
def with_text(text):
    '''route c to text and replace _ with space '''
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def dis_python(text):
    '''display python with value of text'''
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route("/number/<n>", strict_slashes=False)
def display_is_number(n):
    '''display “n is a number” only if n is an integer'''
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return False


if __name__ == '__main__':
    '''main function '''
    app.run(host='0.0.0.0', port=5000)
