# keygenme-py

[keygenme-py](https://play.picoctf.org/practice/challenge/121)

## Description

keygenme-trial.py

## Solution

For this challenge we can download the keygenme-trial.py file and search trought it. We can find an interesting section about activating a license key which is linked to the `key_part_static1_trial` variables. There we can find a function that checks if the given key is valid. It does that by computing a hash on the username and comparing it to the input key. We can use the steps in the check function to leak the key. Instead of comparing to the input key we just print each sha256 hexdigest value in the order from the script and we have the dynamic part of the flag.