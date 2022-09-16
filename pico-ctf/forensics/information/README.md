# information

[information](https://play.picoctf.org/practice/challenge/186)

## Description

Files can always be changed in a secret way. Can you find the flag? cat.jpg

## Solution

Download the image. Open the image in a text editor. There is a field `rdf:resource` in the metadata which contains a string `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` encoded in base 64. Decode the string and obtain the flag.