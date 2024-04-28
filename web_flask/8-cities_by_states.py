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


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    state_cities = {}
    for state in sorted_states:
        if storage.__class__.__name__ == "DBStorage":
            cities = [city for city in state.cities]
            sorted_cities = sorted(cities, key=lambda city: city.name)
        else:
            cities = storage.all(City).values()
            cities = [city for city in cities if city.state_id == state.id]
            sorted_cities = sorted(cities, key=lambda city: city.name)
        state_cities[state.id] = sorted_cities
    return render_template(
            '8-cities_by_states.html',
            sorted_states=sorted_states,
            state_cities=state_cities
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
