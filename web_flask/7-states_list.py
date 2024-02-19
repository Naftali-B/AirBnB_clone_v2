#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays a HTML page with the states listed in alphabetical order.

    Retrieves the states from the storage, sorts them alphabetically, and
    passes them to the template for rendering.
    """
    # Retrieve all states from the storage and sort them alphabetically
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    
    # Render the HTML template and pass the sorted list of states to it
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.

    Ensures that the storage is properly closed to prevent resource leaks
    when the application context is torn down.
    """
    storage.close()

if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' and port '5000'
    app.run(host='0.0.0.0', port='5000')

