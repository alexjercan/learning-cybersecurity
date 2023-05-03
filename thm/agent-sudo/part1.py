#!/bin/python

import sys
import requests

assert len(sys.argv) == 2, "Usage: ./part1.py <user_agent>"

user_agent = sys.argv[1]

url = "http://10.10.63.226/"

headers = {"User-Agent": user_agent}

response = requests.get(url, headers=headers)

print(response.text)
