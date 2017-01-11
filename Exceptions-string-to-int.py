#!/bin/python3

# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

# Exception handling.Trying to cast non-int string to int will yeild
# ValueError
 
try:
    print(int(input().strip()))
except ValueError:
    print("Bad String")
