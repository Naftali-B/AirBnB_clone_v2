#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states():
    """
    Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    # Retrieve all State objects from the storage
    states = storage.all("State")
    
    # Render the HTML template and pass the states to it
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays an HTML page with info about <id>, if it exists.
    """
    # Retrieve the State object with the given id
    state = storage.get("State", id)
    
    # Render the HTML template and pass the state to it
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session.
    """
    # Close the storage to prevent resource leaks
    storage.close()


if __name__ == "__main__":
    # Run the Flask app on host '0.0.0.0' (accessible from any network interface)
    app.run(host="0.0.0.0")

