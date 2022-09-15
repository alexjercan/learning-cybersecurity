# Python Wrangling

[Python Wrangling](https://play.picoctf.org/practice/challenge/166)

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py) using [this password](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt) to get [the flag](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en)?

## Solution

Download all of the given files, then run the `ende.py` python script with the `-d` flag (for decode) passing the `flag.txt.en` as the argument. When the script asks for a password use the text from the `pw.txt` file.