#!/usr/bin/python3
''' a script that starts a Flask web application'''
from markupsafe import escape
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    ''' function with / route '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''function with /HBNB route '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def with_text(text):
    '''function with "/c/<text>" route'''
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
