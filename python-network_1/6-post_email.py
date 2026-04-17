#!/usr/bin/python3
"""Send POST request with email using requests."""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={"email": email})
    print(response.text)
