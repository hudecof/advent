#!/usr/bin/python

import re


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def main():

    length = 0
    for line in read_file('input'):
        match = re.match(r'(\d+)x(\d+)x(\d+)', line)
        l1 = int(match.group(1))
        l2 = int(match.group(2))
        l3 = int(match.group(3))

        length= length + 2*min(l1+l2, l1+l3, l2+l3) + l1*l2*l3

    print length


if __name__ == "__main__":
    main()
