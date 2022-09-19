#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("Usage: ./solve.py <number1> <number2>")
    exit(1)

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

number = max(number1, number2)

print(f"picoCTF{{{number:08x}}}")
