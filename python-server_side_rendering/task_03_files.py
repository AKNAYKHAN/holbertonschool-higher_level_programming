#!/usr/bin/python3
"""Display product data from JSON or CSV files using Flask."""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """Read products from a JSON file."""
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)


def read_csv_file():
    """Read products from a CSV file."""
    products = []

    with open("products.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)

    return products


@app.route("/products")
def products():
    """Display products from JSON or CSV source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        data = read_json_file()
    elif source == "csv":
        data = read_csv_file()
    else:
        return render_template("product_display.html",
                               products=[],
                               error="Wrong source")

    if product_id:
        product_id = int(product_id)
        data = [product for product in data if product["id"] == product_id]

        if not data:
            return render_template("product_display.html",
                                   products=[],
                                   error="Product not found")

    return render_template("product_display.html",
                           products=data,
                           error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
