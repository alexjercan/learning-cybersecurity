#!/bin/sh

binary_url=https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm

wget ${binary_url} -O warm -q

chmod +x warm

./warm -h | grep -o 'picoCTF{.*}'

rm warm