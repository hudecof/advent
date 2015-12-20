#!/usr/bin/python

import re

RE_INGRADIENT_INFO = re.compile(r'^(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$')


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def get_neighbors(lights, posX, posY, minX, minY, maxX, maxY):
    lightsOn = 0
    lightsOff = 0

    for x in range(posX-1, posX+2):
        if x < minX or x > maxX:
            continue
        for y in range(posY-1, posY+2):
            if y < minY or y > maxY:
                continue
            if x == posX and y == posY:
                continue
            if lights[x][y] == '#':
                lightsOn += 1
            if lights[x][y] == '.':
                lightsOff += 1
    return (lightsOn, lightsOff)


def do_one_step(lights, sizeX, sizeY):
    result = []
    for x in range(sizeX):
        line = ""
        for y in range(sizeY):
            light = lights[x][y]
            (on, off) = get_neighbors(lights, x, y, 0, 0, sizeX-1, sizeY-1)
#            print "[%d, %d]: on:%d off: %d" % (x, y, on, off)
            if lights[x][y] == '#':
                if on != 2 and on != 3:
                    light = '.'
            if lights[x][y] == '.':
                if on == 3:
                    light = '#'
            if x == 0 and (y == 0 or y == sizeY-1):
                light = '#'
            if x == sizeX-1 and (y == 0 or y == sizeY-1):
                light = '#'
            line = line + light
        result.append(line)

    return result


def main():
    lights = []
    for line in read_file('input'):
        lights.append(line.strip())

    lights[0] = "#" + lights[0][1:-1] + "#"
    lights[99] = "#" + lights[99][1:-1] + "#"

    for i in range(100):
        print "iteration: %d" % i
        lights = do_one_step(lights, 100, 100)

    on = 0
    for line in lights:
        on += line.count('#')
    print on

if __name__ == "__main__":
    main()
