#!/bin/bash
#script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
