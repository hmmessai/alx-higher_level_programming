#!/bin/bash
# Displays all the HTTP methods the sever will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
