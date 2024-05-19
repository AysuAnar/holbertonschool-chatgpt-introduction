#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

f = factorial(number)
print(f)

