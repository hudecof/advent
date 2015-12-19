#!/usr/bin/python

import re

RE_INGRADIENT_INFO = re.compile(r'^(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$')


class Ingredient:

    def __init__(self, name):
        self.name = name
        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def split_spoons(minCount, maxCount, pos, spoons):
    if pos == len(spoons):
        if sum(spoons) == maxCount:
            yield spoons
        return

    for x in range(minCount, maxCount+1):
        spoons[pos] = x
        for s in split_spoons(minCount, maxCount, pos+1, spoons):
            yield s
    spoons[pos] = minCount


def calculate_score(split, ingrediens):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for x in range(len(split)):
        capacity += split[x]*ingrediens[x].capacity
        durability += split[x]*ingrediens[x].durability
        flavor += split[x]*ingrediens[x].flavor
        texture += split[x]*ingrediens[x].texture
        calories += split[x]*ingrediens[x].calories

    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)

    return (capacity*durability*flavor*texture, calories)


def main():
    ingrediens = []
    spoons = []
    for line in read_file('input'):
        match = re.search(RE_INGRADIENT_INFO, line)
        if not match:
            print "wrong operation syntax"
        i = Ingredient(match.group(1))
        i.capacity = int(match.group(2))
        i.durability = int(match.group(3))
        i.flavor = int(match.group(4))
        i.texture = int(match.group(5))
        i.calories = int(match.group(6))
        ingrediens.append(i)
        spoons.append(0)

    for split in split_spoons(0, 100, 0, spoons):
        (score, calories) = calculate_score(split, ingrediens)
        print "%d %d" % (score, calories)

if __name__ == "__main__":
    main()
