#!/usr/bin/python3

def uppercase(str):
    cap = ''
    for char in str:
        if 'a' <= char <= 'z':
            cap = ord(char) - ord('a') + ord('A')
            print(chr(cap), end="")

        else:
            print(char, end="")
    print()
