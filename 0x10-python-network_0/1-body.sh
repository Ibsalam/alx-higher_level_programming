#!/bin/bash
# Takes in URL, sends GET request to it and displays the response
curl -sX GET "$1" -L 200
