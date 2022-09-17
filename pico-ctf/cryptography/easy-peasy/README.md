# Easy Peasy

[Easy Peasy](https://play.picoctf.org/practice/challenge/125)

## Description

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 20266 otp.py

## Solution

In the `otp.py` script we can see that the encryption method loops around to the start of the key. The encryption method is `XOR` so we know that if we apply it twice on a string we get back the same string, `a ^ b ^ b == a`. First we can get the encrypted key from the initial output of the server. Then we can send 50K - length of the key (32 in bytes) and we are back at the start of the key. Now we can send the encrypted flag as input and get back the decrypted flag. I also tried to send 0 bytes only to try to leak the entire key, but there is not really anything interesting. 