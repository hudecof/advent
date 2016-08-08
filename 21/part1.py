#!/usr/bin/python

import re
from math import ceil

RE_STORE_HEADER = re.compile(r'^(.*):.*$')
RE_STORE_ITEM = re.compile(r'^(.*)\s+(\d+)\s+(\d+)\s+(\d+)')
RE_INPUT = re.compile(r'^(.*):\s+(\d+)$')


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def simulate(me, boss):
    myWinTurns = 0
    bossWinTurns = 0

    myWinTurns = int(ceil(boss['Hit Points'] / max(1, me['Damage'] - boss['Armor'])))
    bossWinTurns = int(ceil(me['Hit Points'] / max(1, boss['Damage'] - me['Armor'])))
    return(myWinTurns, bossWinTurns)


def calculate_possible_combinations(minSum, maxSum, pos, usage):
    if pos == len(usage):
        if sum(usage) >= minSum and sum(usage) <= maxSum:
            yield usage
        return

    for x in range(2):
        usage[pos] = x
        for c in calculate_possible_combinations(minSum, maxSum, pos+1, usage):
            yield c
    usage[pos] = 0


def calculate_sum_product(item, usage, key):
    sum = 0
    for x in range(len(item)):
        sum += item[x][key]*usage[x]
    return sum


def buy(store):
    # 1 Weapon
    # 0-1 Armor
    # 0-2 Rings

    weapons = [0 for x in range(len(store['Weapons']))]
    armor = [0 for x in range(len(store['Armor']))]
    rings = [0 for x in range(len(store['Rings']))]

    for w in calculate_possible_combinations(1, 1, 0, weapons):
        for a in calculate_possible_combinations(0, 1, 0, armor):
            for r in calculate_possible_combinations(0, 2, 0, rings):
                costS = calculate_sum_product(store['Weapons'], w, 'Cost')
                costS += calculate_sum_product(store['Armor'], a, 'Cost')
                costS += calculate_sum_product(store['Rings'], r, 'Cost')
                armorS = calculate_sum_product(store['Weapons'], w, 'Armor')
                armorS += calculate_sum_product(store['Armor'], a, 'Armor')
                armorS += calculate_sum_product(store['Rings'], r, 'Armor')
                damageS = calculate_sum_product(store['Weapons'], w, 'Damage')
                damageS += calculate_sum_product(store['Armor'], a, 'Damage')
                damageS += calculate_sum_product(store['Rings'], r, 'Damage')
                yield (costS, damageS, armorS)


def main():

    boss = dict()
    store = dict()
    me = dict()

    for line in read_file('input'):
        match = re.match(RE_INPUT, line)
        boss[match.group(1)] = int(match.group(2))

    store_group = None
    for line in read_file('store'):
        match = re.match(RE_STORE_HEADER, line)
        if match:
            store_group = match.group(1)
            store[store_group] = []
            continue
        match = re.match(RE_STORE_ITEM, line)
        if match:
            item = dict()
            item['Name'] = match.group(1).strip()
            item['Cost'] = int(match.group(2))
            item['Damage'] = int(match.group(3))
            item['Armor'] = int(match.group(4))
            store[store_group].append(item)

    me['Hit Points'] = 100
    me['Damage'] = 0
    me['Armor'] = 0

    for (c, d, a) in buy(store):
        me['Damage'] = d
        me['Armor'] = a
        (turnMe, trunBoss) = simulate(me, boss)
        if turnMe <= trunBoss:
            print c

if __name__ == "__main__":
    main()
