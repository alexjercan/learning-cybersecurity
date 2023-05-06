# c4ptur3-th3-fl4g

[c4ptur3-th3-fl4g](https://tryhackme.com/room/)

## Solution

### Task 1

1. It is literally just the string but with letters.
2. `"".join(map(lambda s: chr(int(s, 2)), <string>.split(" ")))`
3. `echo <string> | base32 -d`
4. `echo <string> | base64 -d`
5. `"".join(map(lambda s: chr(int(s, 16)), <string>.split(" ")))`
6. `"".join(map(lambda s: chr((ord(s) - ord('a') + 13) % (ord('z') - ord('a') + 1) + ord('a')) if 'a' <= s and s <= 'z' else (chr((ord(s) - ord('A') + 13) % (ord('Z') - ord('A') + 1) + ord('A')) if 'A' <= s and s <= 'Z' else s), <string>))`
7. Rot47, gave up use https://www.dcode.fr/rot-47-cipher
8. Morse Code, https://www.dcode.fr/morse-code
9. `"".join(map(lambda s: chr(int(s)), <string>.split(" ")))`
10. From Base64, From Morse Code, From Binary, ROT47, From Decimal https://gchq.github.io/CyberChef

### Task 2

Use `Audacity`. Load the wav file inside audacity and then press `Shift-M` or
click on `secretaudio` in the menu and select `spectogram` the message should
be written on the image.

### Task 3

Use stehide with an empty passphrase `steghide extract -sf stegosteg.jpg`.

### Task 4

It is enough to run `strings` on the meme.jpg image and the answers are the two
bottom strings.
