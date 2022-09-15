#!/usr/bin/env python3

import socket

hostname = "mercury.picoctf.net"
port = 22902

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostname, port))
    flag = "".join([chr(int(x)) for x in s.recv(1024).decode("ascii").splitlines()])

print(flag, end="")
