#!/bin/sh

script_url=https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py
password_url=https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt
flag_url=https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en

wget ${script_url} -O ende.py
wget ${password_url} -O pw.txt
wget ${flag_url} -O flag.txt.en

cat pw.txt | python ende.py -d flag.txt.en

rm ende.py pw.txt flag.txt.en