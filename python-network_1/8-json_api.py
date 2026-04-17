#!/usr/bin/python3
"""Send POST request and handle JSON response."""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={"q": q})

    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
