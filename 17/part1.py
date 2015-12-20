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


def bottle_usage_positions(minCount, maxCount, pos, usage):
    if pos == len(usage):
        yield usage
        return

    for x in range(minCount, maxCount+1):
        usage[pos] = x
        for b in bottle_usage_positions(minCount, maxCount, pos+1, usage):
            yield b
    usage[pos] = minCount

def calculate_liters(bottles, usage):
    sum = 0
    bottles_used = []
    for x in range(len(bottles)):
        sum += bottles[x] * usage[x]
        bottles_used.append(bottles[x] * usage[x])
    return (sum, bottles_used)


def main():
    input = 150
    bottles = []
    bottle_usage = []
    for line in read_file('input'):
        bottles.append(int(line))
        bottle_usage.append(0)

    for usage in bottle_usage_positions(0, 1, 0, bottle_usage):
        (litres, used) = calculate_liters(bottles, usage)
        if litres == input:
            print used

if __name__ == "__main__":
    main()
