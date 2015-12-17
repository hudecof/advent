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

    size = 0
    for line in read_file('input'):
        match = re.match(r'(\d+)x(\d+)x(\d+)', line)
        s1 = int(match.group(1))*int(match.group(2))
        s2 = int(match.group(1))*int(match.group(3))
        s3 = int(match.group(2))*int(match.group(3))

        size = size + 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)

    print size


if __name__ == "__main__":
    main()
