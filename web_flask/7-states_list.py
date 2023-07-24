#!/usr/bin/python3
"""
a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_appcontext(exception):
    """close the current SQLAlchemy Session After each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def stateList():
    """list all state object (sorted)"""
    states = storage.all(State).values()
    stateSorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=stateSorted)


if __name__ == '__main__':
    """main function"""
    app.run(host='0.0.0.0', port=5000)
