#!/usr/bin/python

import re

RE_SPEED_INFO = re.compile(r'^(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$')


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line

def calculateDistance(time, speed, speedTime, restTime):

    distance = 0
    cycleTime = speedTime + restTime
    cycles = int(time/cycleTime)
    distance = distance + cycles*speed*speedTime

    distance += min(speedTime, time % cycleTime)*speed
    return distance


def main():
    time = 2503
    for line in read_file('input'):
        match = re.search(RE_SPEED_INFO, line)
        if not match:
            print "wrong operation syntax"
        distance = calculateDistance(time, int(match.group(2)), int(match.group(3)), int(match.group(4)))
        print "%010d %s" % (distance, match.group(1))

if __name__ == "__main__":
    main()
