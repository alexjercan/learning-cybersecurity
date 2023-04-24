# MacroHard WeakEdge

[MacroHard WeakEdge](https://play.picoctf.org/practice/challenge/130)

## Description

I've hidden a flag in this file. Can you find it? Forensics is fun.pptm

## Solution

Download the file. It looks like a ppt that has macros so maybe we can use
`binwalk` to extract hidden files.

One idea is to search for a file called `hidden` since this is a hint in the
description. So we can run `find . | grep hidden` and we find one file
`./_Forensics is fun.pptm.extracted/ppt/slideMasters/hidden`.

I found a cool command `find . -type f -name "*hidden*" -exec cat {} +` that
prints the contents for the hidden file.

The final command is `find . -type f -name "*hidden*" -exec cat {} + | tr -d
[:space:] | base64 --decode` but I have no idea how to fix it because there is
some trash character, maybe \r that I cannot remove in the file.

Or just run `solve.sh` to get a flag.
