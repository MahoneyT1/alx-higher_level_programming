#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total = 0

    length = len(argv) - 1

    if length == 0:
        total = 0
        print(total)

    elif length == 1:
        total = int(argv[length])
        print(total)

    elif length > 1:
        for i in range(1, len(argv)):
            total = total + int(argv[i])

        print(total)
