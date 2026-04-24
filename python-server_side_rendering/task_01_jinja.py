#!/usr/bin/python3
"""Basic Flask application using Jinja templates."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render contact page."""
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
