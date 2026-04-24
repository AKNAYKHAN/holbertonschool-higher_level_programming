#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite using Flask."""

import csv
import json
import sqlite3
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


def read_sql_database():
    """Read products from SQLite database."""
    products = []

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    return products


@app.route("/products")
def products():
    """Display products from selected data source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            data = read_json_file()
        elif source == "csv":
            data = read_csv_file()
        elif source == "sql":
            data = read_sql_database()
        else:
            return render_template("product_display.html",
                                   products=[],
                                   error="Wrong source")

        if product_id:
            product_id = int(product_id)
            data = [item for item in data if item["id"] == product_id]

            if not data:
                return render_template("product_display.html",
                                       products=[],
                                       error="Product not found")

        return render_template("product_display.html",
                               products=data,
                               error=None)

    except sqlite3.Error:
        return render_template("product_display.html",
                               products=[],
                               error="Database error")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
