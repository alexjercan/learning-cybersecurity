#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Usage $0 \"<name>\""
    exit 1
fi

wget https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg -q -O garden.jpg 

echo $(strings garden.jpg | grep -o "picoCTF{.*}")

rm garden.jpg
