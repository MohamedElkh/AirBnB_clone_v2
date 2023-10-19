#!/usr/bin/python3
"""the app listen on 0000, port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """func to display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """func to display HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
