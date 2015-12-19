#!/usr/bin/python

import re

RE_HAPPY = re.compile(r'^(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*).')


class Person:

    def __init__(self, name):
        self.name = name
        self.happiness = dict()

    def addNeighborHappyness(self, name, value):
        self.happiness[name] = value


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def getNeighborHappyness(persons, p1, p2):
    h1 = persons[p1].happiness[p2]
    h2 = persons[p2].happiness[p1]
    return h1 + h2

def computeHappiness(personList, personSitting, happyness):
    # empty list
    if len(personSitting) == 0:
        personSitting.insert(0, personList.keys()[0])
        computeHappiness(personList, personSitting, happyness)
        personSitting.pop(0)
        return

    # full list
    if len(personList.keys()) == len(personSitting):
        p1 = personSitting[0]
        p2 = personSitting[len(personSitting)-1]
        happyness += getNeighborHappyness(personList, p1, p2)
        print "%010d %s" % (happyness, ", ".join(personSitting))
        happyness -= getNeighborHappyness(personList, p1, p2)
        return

    firstPerson = personSitting[0]
    for neighbor in personList[firstPerson].happiness.keys():
        if neighbor in personSitting:
            continue
        personSitting.insert(0, neighbor)
        happyness += getNeighborHappyness(personList, firstPerson, neighbor)
        computeHappiness(personList, personSitting, happyness)
        personSitting.pop(0)
        happyness -= getNeighborHappyness(personList, firstPerson, neighbor)


def main():
    persons = dict()
    for line in read_file('input'):
        match = re.search(RE_HAPPY, line)
        if not match:
            print "wrong operation syntax"
        if match.group(1) not in persons:
            persons[match.group(1)] = Person(match.group(1))
        happynnes = int(match.group(3))
        if match.group(2) == "lose":
            happynnes = happynnes * -1
        persons[match.group(1)].addNeighborHappyness(match.group(4), happynnes)

    computeHappiness(persons, [], 0)


if __name__ == "__main__":
    main()
