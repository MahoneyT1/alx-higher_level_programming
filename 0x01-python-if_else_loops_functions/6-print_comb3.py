#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        print(f'{i}{j}'.format(), end=", " if i < 8 else "")
print()
