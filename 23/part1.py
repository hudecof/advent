#!/usr/bin/python

import re

RE_INSTR01 = re.compile(r'^(jio|jie) (a|b), ((\+|-)\d+)$')
RE_INSTR02 = re.compile(r'^(inc|tpl|hlf) (a|b)$')
RE_INSTR03 = re.compile(r'^(jmp) ((\+|-)\d+)$')


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line

def run_program(instrustions, a=0, b=0):
    register = dict()
    register['a'] = a
    register['b'] = b
    pos = 0


    while True:
        try:
            i = instrustions[pos]
        except IndexError:
            break

        if i[0] == 'hlf':
            register[i[1]] = register[i[1]]/2
            pos += 1
            continue
        if i[0] == 'tpl':
            register[i[1]] = register[i[1]]*3
            pos += 1
            continue
        if i[0] == 'inc':
            register[i[1]] += 1
            pos  += 1
            continue
        if i[0] == 'jmp':
            pos += i[1]
            continue
        if i[0] == 'jie':
            if register[i[1]] % 2 == 0:
                pos += i[2]
                continue
            pos += 1
            continue
        if i[0] == 'jio':
            if register[i[1]] == 1:
                pos += i[2]
                continue
            pos += 1
            continue

        print i[0]

    return (register['a'], register['b'])


def main():
    instructions = []
    for line in read_file('input'):
        match = re.match(RE_INSTR01,  line)
        if match:
            instructions.append((match.group(1), match.group(2), int(match.group(3))))
        match = re.match(RE_INSTR02,  line)
        if match:
            instructions.append((match.group(1), match.group(2)))
        match = re.match(RE_INSTR03,  line)
        if match:
            instructions.append((match.group(1), int(match.group(2))))

    print run_program(instructions)

if __name__ == "__main__":
    main()
