#!/usr/bin/env python3
import socket

def recv_until(s, delim):
    data = b''
    while not data.endswith(delim):
        data += s.recv(1)
    return data


hostname = "mercury.picoctf.net"
port = 59953


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostname, port))

    gcode = b''
    for i in range(1126):
        gcode += recv_until(s, b"\n")

print(gcode.decode("utf-8"))