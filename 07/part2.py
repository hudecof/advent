#!/usr/bin/python

import re

RE_WIRE = re.compile(r'^(.*) -> (.*)$')
RE_OPER_NOT = re.compile(r'^NOT (.*)$')
RE_OPER_AND = re.compile(r'^(.*) AND (.*)$')
RE_OPER_OR = re.compile(r'^(.*) OR (.*)$')
RE_OPER_LSHIFT = re.compile(r'^(.*) LSHIFT (.*)$')
RE_OPER_RSHIFT = re.compile(r'^(.*) RSHIFT (.*)$')
RE_OPER_VALUE = re.compile(r'^(\d+)$')
RE_OPER_COPY = re.compile(r'^([a-z]+)$')


class Wire:

    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.value = None


def getWireVaule(name, wires):

    if re.search(RE_OPER_VALUE, name):
        return int(name)

    if wires[name].value:
        return wires[name].value

    print "*%s -> %s" % (wires[name].source, wires[name].name)
    # test on value
    match = re.search(RE_OPER_VALUE, wires[name].source)
    if match:
        wires[name].value = int(match.group(1))

    match = re.search(RE_OPER_COPY, wires[name].source)
    if match:
        value = getWireVaule(match.group(1), wires)
        wires[name].value = value

    match = re.search(RE_OPER_NOT, wires[name].source)
    if match:
        value = getWireVaule(match.group(1), wires)
        wires[name].value = ~value & 0xFFFF

    match = re.search(RE_OPER_AND, wires[name].source)
    if match:
        value1 = getWireVaule(match.group(1), wires)
        value2 = getWireVaule(match.group(2), wires)
        wires[name].value = value1 & value2

    match = re.search(RE_OPER_OR, wires[name].source)
    if match:
        value1 = getWireVaule(match.group(1), wires)
        value2 = getWireVaule(match.group(2), wires)
        wires[name].value = value1 | value2

    match = re.search(RE_OPER_LSHIFT, wires[name].source)
    if match:
        value1 = getWireVaule(match.group(1), wires)
        value2 = int(match.group(2))
        wires[name].value = (value1 << value2) & 0xFFFF

    match = re.search(RE_OPER_RSHIFT, wires[name].source)
    if match:
        value1 = getWireVaule(match.group(1), wires)
        value2 = int(match.group(2))
        wires[name].value = (value1 >> value2) & 0xFFFF

    return wires[name].value


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def main():
    wire = dict()
    for line in read_file('input'):
        match = re.search(RE_WIRE, line)
        if not match:
            print "wrong operation syntax"
        wire[match.group(2)] = Wire(match.group(2), match.group(1))

    value_a = getWireVaule("a", wire)
    for key in wire.keys():
        wire[key].value = None
    wire["b"].value = value_a
    print getWireVaule("a", wire)

if __name__ == "__main__":
    main()
