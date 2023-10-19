#!/usr/bin/python3
"""start app flask"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """func to display main hb"""
    states = storage.all("State")
    amenities = storage.all("Amenity")

    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """func to remove the current sql"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
