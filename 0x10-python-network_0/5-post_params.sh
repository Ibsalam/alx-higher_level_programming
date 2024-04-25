#!/bin/bash
# takes in a URL and sends a POST
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
