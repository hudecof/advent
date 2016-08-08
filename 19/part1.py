#!/usr/bin/python

import re

RE_RULE = re.compile(r'^(.*) => (.*)$')


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line.strip()


def apply_rule(formula, key, value):
    keyLen = len(key)
    formulaPos = 0

#    print "formula: %s, key: %s, value: %s" % (formula, key, value)
    while True:
        pos = formula.find(key, formulaPos)
#        print " - pos: %d" % (pos)
        if pos < 0:
            break
        yield formula[0:pos] + value + formula[pos+keyLen:]
        formulaPos = pos + keyLen


def main():
    formula = ""
    rules = dict()
    for line in read_file('input'):
        # skip empty lines
        if not line:
            continue
        match = re.match(RE_RULE, line)
        if match:
            if match.group(1) not in rules:
                rules[match.group(1)] = []
            rules[match.group(1)].append(match.group(2))
        else:
            formula = line

    for k1, v1 in rules.iteritems():
        for v2 in v1:
            for r in apply_rule(formula, k1, v2):
                print r


if __name__ == "__main__":
    main()
