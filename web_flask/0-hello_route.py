#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello HBNB!"


app.run(debug=True, strict_slashes=False, port=5000, host='0.0.0.0')
