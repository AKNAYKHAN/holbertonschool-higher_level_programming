#!/usr/bin/python3
"""Get GitHub user id using Basic Authentication."""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(username, token))
    data = response.json()

    print(data.get("id"))
