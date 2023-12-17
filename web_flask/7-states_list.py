#!/usr/bin/python3
"script that starts a Flask web application"
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", storage=storage.all(State))


@app.teardown_appcontext
def teardown():
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
