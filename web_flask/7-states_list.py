#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Closes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template(
            '7-states_list.html',
            sorted_states=sorted_states
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
