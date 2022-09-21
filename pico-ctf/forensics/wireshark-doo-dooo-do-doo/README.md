# Wireshark doo dooo do doo...

[Wireshark doo dooo do doo...](https://play.picoctf.org/practice/challenge/115)

## Description

Can you find the flag? shark1.pcapng.

## Solution

We can open the shark1.pcapng in wireshark. Follow TCP streams to see the requests made by the client. If we go trought them we find that the stream 5 `tcp.stream eq 5` contains a string `Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}` which resembles a flag structure. We decode with ROT13 and we obtain the flag.