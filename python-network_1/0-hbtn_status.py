#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    body = response.read()

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
