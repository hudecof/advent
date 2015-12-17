#!/usr/bin/python

import re


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def count_twice(line):
    regexp = re.compile(r"(..).*\1")
    match = re.search(regexp, line)
    if match:
        return True
    return False


def count_repeat(line):
    regexp = re.compile(r"(.).\1")
    match = re.search(regexp, line)
    if match:
        return True
    return False


def main():
    nice = 0
    for line in read_file('input'):
        if not count_twice(line):
            continue
        if not count_repeat(line):
            continue
        nice = nice + 1

    print nice

if __name__ == "__main__":
    main()
