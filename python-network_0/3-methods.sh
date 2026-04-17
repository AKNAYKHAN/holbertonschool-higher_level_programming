#!/bin/bash
# Display allowed HTTP methods
curl -sI "$1" | grep -i Allow | cut -d' ' -f2-
