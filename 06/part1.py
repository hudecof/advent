#!/usr/bin/python

import re


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def getPosKey(posX, posY):
    return "%03d%03d" % (posX, posY)


def action_turn_on(data, posX1, posY1, posX2, posY2):
    changed = 0
    for posX in range(posX1, posX2+1):
        for posY in range(posY1, posY2+1):
            key = getPosKey(posX, posY)
            if key not in data:
                data[key] = False
            if not data[key]:
                data[key] = True
                changed = changed + 1
    return (data, changed, 0)


def action_turn_off(data, posX1, posY1, posX2, posY2):
    changed = 0
    for posX in range(posX1, posX2+1):
        for posY in range(posY1, posY2+1):
            key = getPosKey(posX, posY)
            if key not in data:
                data[key] = False
            if data[key]:
                data[key] = False
                changed = changed + 1
    return (data, 0, changed)


def action_toggle(data, posX1, posY1, posX2, posY2):
    changedOn = 0
    changedOff = 0

    for posX in range(posX1, posX2+1):
        for posY in range(posY1, posY2+1):
            key = getPosKey(posX, posY)
            if key not in data:
                data[key] = False
            if not data[key]:
                data[key] = True
                changedOn = changedOn + 1
            else:
                data[key] = False
                changedOff = changedOff + 1

    return (data, changedOn, changedOff)


def main():
    RE_COORD = re.compile(r" (\d+),(\d+) through (\d+),(\d+)$")
    lOn = 0
    grid = dict()
    for line in read_file('input'):
        match = re.search(RE_COORD, line)
        posX1 = (int)(match.group(1))
        posY1 = (int)(match.group(2))
        posX2 = (int)(match.group(3))
        posY2 = (int)(match.group(4))
        changedOn = 0
        changedOff = 0
        if line.startswith("turn on "):
            (grid, changedOn, changedOff) = action_turn_on(grid, posX1, posY1, posX2, posY2)
        if line.startswith("turn off "):
            (grid, changedOn, changedOff) = action_turn_off(grid, posX1, posY1, posX2, posY2)
        if line.startswith("toggle "):
            (grid, changedOn, changedOff) = action_toggle(grid, posX1, posY1, posX2, posY2)
        lOn = lOn + changedOn - changedOff

    print lOn


if __name__ == "__main__":
    main()
