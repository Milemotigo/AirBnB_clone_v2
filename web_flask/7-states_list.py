#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage, State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


Session = scoped_session(sessionmaker(bind=storage._engine))


@app.teardown_appcontext
def close_session(exception=None):
    """Close the current SQLAlchemy Session after each request."""
    Session.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with the list of all State objects sorted by."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
