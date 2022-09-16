#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Usage $0 <url>"
    exit 1
fi

wget $1 -O Addadshashanammu.zip -q
unzip -q Addadshashanammu.zip

echo $(strings $(find ./Addadshashanammu -type f | xargs ls) | grep -o 'picoCTF{.*}')

rm -rf Addadshashanammu.zip Addadshashanammu
