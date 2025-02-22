#!/usr/bin/python3

''' starts a Flask web app '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ / displays 'Hello HBNB' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ /hbnb displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ displays C followed by value of text passed """
    return f'C {text.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """ displays Python followed by value of text """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
