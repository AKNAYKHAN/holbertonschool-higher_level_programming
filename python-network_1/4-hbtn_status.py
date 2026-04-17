#!/usr/bin/python3
"""Fetch status using requests."""

import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
