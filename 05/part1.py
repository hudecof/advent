#!/usr/bin/python

import re


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def count_vovels(line):
    count = 0
    for vovel in ['a', 'e', 'i', 'o', 'u']:
        count = count + line.count(vovel)
    return count


def count_bad(line):
    count = 0
    for vovel in ['ab', 'cd', 'pq', 'xy']:
        count = count + line.count(vovel)
    return count

def count_double(line):
    regexp = re.compile(r"(.)\1")
    match = re.search(regexp, line)
    if match:
        return 1
    return 0

def main():
    nice = 0
    for line in read_file('input'):
        if count_vovels(line) < 3:
            continue
        if count_double(line) < 1:
            continue
        if count_bad(line) > 0:
            continue
        nice = nice + 1

    print nice

if __name__ == "__main__":
    main()
