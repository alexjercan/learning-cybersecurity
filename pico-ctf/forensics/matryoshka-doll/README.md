# Matryoshka doll

[Matryoshka doll](https://play.picoctf.org/practice/challenge/129)

## Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this

## Solution

For this task we can use binwalk to extract the hidden files from the image. Each image that we extract will contain another hidden image that we can furhter binwalk until we get a txt file with the flag.