#!/usr/bin/python3
for ch in reversed(range(65, 91)):
    print("{:c}".format(ch if (ch % 2 == 1) else (ch + 32)), end='')
