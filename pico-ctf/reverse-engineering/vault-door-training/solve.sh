#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Usage $0 <url>"
    exit 1
fi

wget $1 -q -O VaultDoorTraining.java

printf "picoCTF{%s}\n" $(cat VaultDoorTraining.java | grep -oP '(?<=equals\(").*(?="\))')

rm VaultDoorTraining.java

