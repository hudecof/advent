#!/usr/bin/python

import re

RE_DISTANCE = re.compile(r'^(.*) to (.*) = (\d+)$')


class Town:

    def __init__(self, name):
        self.name = name
        self.distance = dict()

    def addDistance(self, town, distance):
        self.distance[town] = distance


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def computePossiblePaths(town, neighbours, maxTowns, visited, journey):
    visited.append(town)
    if len(visited) == maxTowns:
        print "%010d %s" % (journey, ",".join(visited))
        visited.pop()
        return
    for nei in neighbours[town].distance.keys():
        if nei in visited:
            continue
        distance = neighbours[town].distance[nei]
        journey += distance
        computePossiblePaths(nei, neighbours, maxTowns, visited, journey)
        journey -= distance
    visited.pop()


def main():
    towns = dict()
    for line in read_file('input'):
        match = re.search(RE_DISTANCE, line)
        if not match:
            print "wrong operation syntax"
        if match.group(1) not in towns:
            towns[match.group(1)] = Town(match.group(1))
        if match.group(2) not in towns:
            towns[match.group(2)] = Town(match.group(2))
        towns[match.group(1)].addDistance(match.group(2), int(match.group(3)))
        towns[match.group(2)].addDistance(match.group(1), int(match.group(3)))

    for town in towns.keys():
        print "Starting point: %s" % (town)
        computePossiblePaths(town, towns, len(towns.keys()), [], 0)

if __name__ == "__main__":
    main()
