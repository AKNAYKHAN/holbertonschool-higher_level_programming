#!/bin/bash
# Display size of response body in bytes
curl -s "$1" | wc -c
