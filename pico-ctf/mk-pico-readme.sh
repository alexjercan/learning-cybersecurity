#!/bin/sh
if [ "$#" -ne 2 ]; then
    echo "Usage $0 \"<category>\" \"<name>\""
    exit 1
fi

category=$1
name=$2

prefix=$(echo -n $category | tr -c "[:alnum:]" "-" | tr '[:upper:]' '[:lower:]')
dirname=$prefix/$(echo -n $name | tr -c "[:alnum:]" "-" | tr '[:upper:]' '[:lower:]')

mkdir -p $dirname
cd $dirname

echo "# $name\n\n[$name](https://play.picoctf.org/practice/challenge/)\n\n## Description\n\n## Solution\n
" > README.md

if command -v tmux-sessionizer &> /dev/null
then
    tmux-sessionizer $(pwd)
fi

