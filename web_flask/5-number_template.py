#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Return a string "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return a string "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_textt(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>')
@app.route('/python/')
def display_text(text='is_cool'):
    """
    The default value of text is “is cool”
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>')
def display_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def display_number_template(n):
    if isinstance(n, int):
        return render_template('number.html', number=n)
    else:
        return 'Error: Not an integer'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
