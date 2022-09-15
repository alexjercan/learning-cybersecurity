import urllib.request

url="https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc"

with urllib.request.urlopen(url) as response:
    enc = response.read().decode("utf-8")

dec = ""

for c in enc:
    c1 = ord(c) >> 8 & 0xff
    c2 = ord(c) & 0xff
    dec += chr(c1) + chr(c2)

print(dec)
