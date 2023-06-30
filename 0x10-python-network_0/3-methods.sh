#!/bin/bash
# Displays all the HTTP methods the sever will accept
curl -sX OPTIONS -i "$1" | grep "Allow" | cut -d " " -f 2-
