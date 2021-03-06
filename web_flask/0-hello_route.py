#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route("/")
@app.route("/airbnb-onepage/")
def index():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
