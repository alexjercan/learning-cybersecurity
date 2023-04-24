#!/bin/bash

url=https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensics%20is%20fun.pptm

wget --quiet https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensics%20is%20fun.pptm -O fun.pptm

binwalk -eq fun.pptm

echo $(find . -type f -name "*hidden*" -exec cat {} + | tr -d [:space:] | base64 -i --decode 2> /dev/null | sed "s/flag: //")

rm -rf fun.pptm _fun.pptm.extracted/
