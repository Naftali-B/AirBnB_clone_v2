#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBnB filters HTML page.

    Retrieves all states and amenities from the storage
    and passes them to the template for rendering.
    """
    # Retrieve all State and Amenity objects from the storage
    states = storage.all("State")
    amenities = storage.all("Amenity")
    
    # Render the HTML template and pass the states and amenities to it
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session.

    Ensures that the SQLAlchemy session is properly closed to prevent
    resource leaks when the application context is torn down.
    """
    # Close the storage to prevent resource leaks
    storage.close()


if __name__ == "__main__":
    # Run the Flask app on host '0.0.0.0' (accessible from any network interface)
    app.run(host="0.0.0.0")

