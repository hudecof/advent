#!/usr/bin/python

import re

RE_SPEED_INFO = re.compile(r'^(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$')

class Reindeer:

    def __init__(self, name):
        self.name = name
        self.speed = None
        self.speedTime = None
        self.restTime = None
        self.points = 0

    def addPoint(self):
            self.points += 1

    def calculateDistance(self, time):

        distance = 0
        cycleTime = self.speedTime + self.restTime
        cycles = int(time/cycleTime)
        distance = distance + cycles*self.speed*self.speedTime

        distance += min(self.speedTime, time % cycleTime)*self.speed
        return distance


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def main():
    time = 2503
    reindeers = dict()
    distance = dict()

    for line in read_file('input'):
        match = re.search(RE_SPEED_INFO, line)
        if not match:
            print "wrong operation syntax"
        reindeers[match.group(1)] = Reindeer(match.group(1))
        reindeers[match.group(1)].speed = int(match.group(2))
        reindeers[match.group(1)].speedTime = int(match.group(3))
        reindeers[match.group(1)].restTime = int(match.group(4))
        distance[match.group(1)] = 0

    for t in range(2503):
        maxDistance = 0
        for r,v in reindeers.iteritems():
            distance[r] = v.calculateDistance(t+1)
            maxDistance = max(maxDistance, distance[r])
        for r,v in distance.iteritems():
            if v == maxDistance:
                    reindeers[r].addPoint()


    for r,v in reindeers.iteritems():
        print "%010d %s" % (v.points, r)

if __name__ == "__main__":
    main()
