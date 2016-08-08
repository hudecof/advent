#!/usr/bin/python

# solution borrowd from
# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/?sort=new

import re
from random import shuffle

RE_RULE = re.compile(r'^(.*) => (.*)$')


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line.strip()

def find_formula(formula, rules):
    steps = 0
    f = formula
    while formula != 'e':
        start = formula
        for k,v in rules:
            if v in formula:
                steps += 1
                formula = formula.replace(v, k, 1)

        if formula == start:
            shuffle(rules)
            steps = 0
            formula = f

    return steps

def main():
    medicine = ""
    rules = []
    for line in read_file('input'):
        # skip empty lines
        if not line:
            continue
        match = re.match(RE_RULE, line)
        if match:
            rules.append((match.group(1), match.group(2)))
        else:
            medicine = line

    print rules
    print medicine
    print find_formula(medicine, rules)

if __name__ == "__main__":
    main()
