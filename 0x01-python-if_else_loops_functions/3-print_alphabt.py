#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if chr(i) == 'q' and chr(i) == 'e':
        continue
    print(chr(i).format().lower(), end="")
