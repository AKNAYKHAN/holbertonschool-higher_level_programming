#!/usr/bin/python3
"""Flask application with dynamic Jinja template logic."""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/items")
def items():
    """Render items page using data from JSON file."""
    with open("items.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return render_template("items.html", items=data.get("items", []))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
