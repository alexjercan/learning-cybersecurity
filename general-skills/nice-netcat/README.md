# Nice netcat...

[Nice netcat...](https://play.picoctf.org/practice/challenge/156)

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22902`, but it doesn't speak English...

## Solution

The response of the server are characters in ascii format. Convert each one of them into characters and obtain the flag.