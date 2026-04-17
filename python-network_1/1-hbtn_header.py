#!/usr/bin/python3
"""Fetch and display the X-Request-Id header value from a URL."""

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
