#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Closes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def show_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', sorted_states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def show_state(state_id):
    if storage.__class__.__name__ == "DBStorage":
        session = storage._DBStorage__session
        states_list = session.query(State).filter(State.id == state_id)
        state = states_list[0]
    else:
        state = storage.get(State, state_id)
    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
