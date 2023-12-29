#!/usr/bin/python3

def uppercase(str):
    cap = ''
    for char in str:
        if 'a' <= char <= 'z':
            cap = ord(char) - ord('a') + ord('A')
            print("{}".format(chr(cap)), end="")

        else:
            print("{}".format(char), end="")
    print()
