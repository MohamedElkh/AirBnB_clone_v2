#!/usr/bin/python3
"""start flask app on port 5000"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """func to display html page"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """func to remove the currentt sql"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
