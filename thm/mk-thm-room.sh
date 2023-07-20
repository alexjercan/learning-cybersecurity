#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage $0 \"<id>\""
    exit 1
fi

id=$1

dirname=$(echo -n $id | tr -c "[:alnum:]" "-" | tr '[:upper:]' '[:lower:]')

if [ ! -d $dirname ]
then
    mkdir -p $dirname

    printf "# \n\n[TryHackMe Room](https://tryhackme.com/room/$id)\n\n## Solution\n" > $dirname/README.md
fi

cd $dirname


if command -v tmux-sessionizer &> /dev/null
then
    tmux-sessionizer $(pwd)
fi

