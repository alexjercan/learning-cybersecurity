#!/usr/bin/env python3
numbers = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

characters = [
    (chr(ord('a') + i - 1)  if i != '{' and i != '}' else i) for i in numbers
]

print("".join(characters).upper())
