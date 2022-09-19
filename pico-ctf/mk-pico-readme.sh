#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Usage $0 \"<name>\""
    exit 1
fi

name=$1
dirname=$(echo -n $name | tr -c "[:alnum:]" "-" | tr '[:upper:]' '[:lower:]')

mkdir -p $dirname
cd $dirname

echo "# $name\n\n[$name](https://play.picoctf.org/practice/challenge/)\n\n## Description\n\n## Solution\n
" > README.md
