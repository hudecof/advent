#!/usr/bin/python

import re

RE_PARSE = re.compile(r'.* (\d+),.* (\d+).$')

def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def get_position(row, col):
    triangle = (row + col-1) * (row + col) / 2
    return triangle - row + 1


def main():
    code_first = 20151125
    code_mul = 252533
    code_mod = 33554393

    for line in read_file('input'):
        match = re.match(RE_PARSE, line)
        row = int(match.group(1))
        col = int(match.group(2))
        code = code_first
        iterations = get_position(row, col)
        for x in range(iterations-1):
            code = (code * code_mul) % code_mod
        print code

if __name__ == "__main__":
    main()

