#!/usr/bin/python3
''' a script that starts a Flask web application'''

from flask import Flask
app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    ''' function with / route '''
    return "Hello HBNB!"


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
