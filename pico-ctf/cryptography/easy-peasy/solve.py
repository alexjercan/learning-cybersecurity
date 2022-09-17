#!/usr/bin/env python3
import socket

KEY_LEN = 50000

def recv_until(s, delim):
    data = b''
    while not data.endswith(delim):
        data += s.recv(1)
    return data

hostname = "mercury.picoctf.net"
port = 20266


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostname, port))

    recv_until(s, b"This is the encrypted flag!\n")

    encrypted_flag = bytes.fromhex(recv_until(s, b"\n")[:-1].decode('utf-8'))

    recv_until(s, b"What data would you like to encrypt? ")

    payload = ('\x00' * (KEY_LEN - len(encrypted_flag)) + '\n').encode('utf-8')
    s.send(payload)

    recv_until(s, b"What data would you like to encrypt? ")

    payload = encrypted_flag + b'\n'
    s.send(payload)

    recv_until(s, b"Here ya go!\n")

    flag = bytes.fromhex(recv_until(s, b"\n")[:-1].decode('utf-8')).decode('utf-8')

print(f"picoCTF{{{flag}}}")