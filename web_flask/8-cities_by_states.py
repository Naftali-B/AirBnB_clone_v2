#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with a list of all states and related cities.

    Retrieves all states from the storage, along with their related cities,
    sorts them alphabetically, and passes them to the template for rendering.
    """
    # Retrieve all states and related cities from the storage
    states = storage.all("State")
    
    # Render the HTML template and pass the states to it
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session.

    Ensures that the SQLAlchemy session is properly closed to prevent
    resource leaks when the application context is torn down.
    """
    storage.close()


if __name__ == "__main__":
    # Run the Flask app on host '0.0.0.0' (accessible from any network interface)
    app.run(host="0.0.0.0")

