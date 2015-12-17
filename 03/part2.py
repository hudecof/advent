#!/usr/bin/python


def read_file(filename, chunk=1024):
    file = open(filename, 'r')
    while True:
        line = file.read(chunk)
        if not line:
            break
        yield line


def getFloorPlanKey(posX, posY):
    return "%dx%d" % (posX, posY)


def moveSanta(posX, posY, direction):
    if direction == '>':
        posX = posX + 1
    if direction == '<':
        posX = posX - 1
    if direction == '^':
        posY = posY + 1
    if direction == 'v':
        posY = posY - 1
    return (posX, posY)


def main():
    posX1 = 0
    posY1 = 0
    posX2 = 0
    posY2 = 0
    houses = 1
    floorPlan = dict()
    floorPlan[getFloorPlanKey(0, 0)] = 1

    for line in read_file('input', 2):

        (posX1, posY1) = moveSanta(posX1, posY1, line[0])
        key1 = getFloorPlanKey(posX1, posY1)
        if key1 not in floorPlan:
            houses = houses + 1
            floorPlan[key1] = 0
        floorPlan[key1] = floorPlan[key1] + 1

        if len(line) < 2:
            break

        (posX2, posY2) = moveSanta(posX2, posY2, line[1])
        key2 = getFloorPlanKey(posX2, posY2)

        if key2 not in floorPlan:
            houses = houses + 1
            floorPlan[key2] = 0
        floorPlan[key2] = floorPlan[key2] + 1

    print houses

if __name__ == "__main__":
    main()
