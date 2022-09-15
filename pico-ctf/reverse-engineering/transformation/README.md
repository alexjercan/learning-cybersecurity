# Transformation

[Transformation](https://play.picoctf.org/practice/challenge/104)

## Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

## Solution

If we download the encoded string we can see that it contains non ascii characters, so we can assume that the command from the description was used on the flag to generate that string. We can reverse engineer that command so that each character of the encoded string is converted into two ascii characters by doing `ord(enc[i]) >> 8 & 0xFF` and `ord(enc[i]) & 0xFF`.