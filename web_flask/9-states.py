#!/usr/bin/python3
"""start flask app on port 5000"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def func_states():
    """func to display html page"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def func_states_id(id):
    """func to display html page"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def func_teardown(exc):
    """fucn to remove the current sql"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
