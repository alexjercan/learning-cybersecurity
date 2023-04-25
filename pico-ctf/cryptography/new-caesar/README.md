# New Caesar

[New Caesar](https://play.picoctf.org/practice/challenge/158)

## Description

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm new_caesar.py

## Solution

I just used the new_caesar.py file to figure out how to reverse the cypher.

First I unshifted the encrypted text (substract the key from the char).
Then, for decode, each character from the plain text was converted into two
characters from a->p. So it is similar to converting it to base 16, but instead
of digits it uses letters. So I did just that, first letter represents the high
part of the byte and the second letter is the rhs of the byte. Concatenate them
and convert to number, that number is the ord of the letter.
To do full decode you have to unshift and then b16_decode.

idk how I was supposed to get the key, but in the code we can see that it must
have length 1, so I bruteforced it.

```bash
echo "YOUR_ENC_TEXT" | python solve.py -k "YOUR_KEY" decode | xargs printf "picoCTF{%s}"
```
