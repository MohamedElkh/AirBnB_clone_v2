#!/usr/bin/python3
"""start flask app on port 5000"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def func_states_list():
    """func to display html page"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def func_teardown(exc):
    """func to remove the current sql"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
