#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage $0 \"<name>\""
    exit 1
fi

name=$1

dirname=$(echo -n $name | tr -c "[:alnum:]" "-" | tr '[:upper:]' '[:lower:]')

if [ ! -d $dirname ]
then
    mkdir -p $dirname

    printf "# $name\n\n[$name](https://tryhackme.com/room/)\n\n## Solution\n" > $dirname/README.md
fi

cd $dirname


if command -v tmux-sessionizer &> /dev/null
then
    tmux-sessionizer $(pwd)
fi

