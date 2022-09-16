# Static ain't always noise

[Static ain't always noise](https://play.picoctf.org/practice/challenge/163)

## Description

Can you look at the data in this binary: static? This BASH script might help!

## Solution

Download the static file and the bash script. You can either run the bash script using the static file as argument and then look for the picCTF{.*} flag or just run `strings tatic | grep picoCTF`.