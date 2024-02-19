#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays a HTML page like 8-index.html."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('100-hbnb.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

