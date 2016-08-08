#!/usr/bin/python

import re
from copy import deepcopy
from sys import maxsize

RE_INPUT = re.compile(r'^(.*):\s+(\d+)$')

spells = [
    {'name': 'Magic Missile', 'costs': 53, 'damage': 4, 'turns': 0},
    {'name': 'Drain', 'costs': 73, 'damage': 2, 'heal': 2, 'turns': 0},
    {'name': 'Shield', 'costs': 113, 'armor':  7, 'turns': 6},
    {'name': 'Poison', 'costs': 173, 'damage': 3, 'turns': 6},
    {'name': 'Recharge', 'costs': 229, 'mana': 101, 'turns': 5}
]
minManaUsed = maxsize

def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line

def printSpells(s):
    name = []
    for (s1,t1) in s:
        name.append("%s (%d)" % (spells[s1]['name'], t1))
    print ", ".join(name)

def sim(me, boss, activeSpells, meTurn, manaUsed):
    global minManaUsed

    newSpells = []
    newBoss = deepcopy(boss)
    newMe = deepcopy(me)

    newMe['Armor'] = 0

    newMe['Hit Points'] -= 1
    if newMe['Hit Points'] <= 0:
        return False

    for (s, t) in activeSpells:
        if t >= 0:
            newBoss['Hit Points'] -= spells[s]['damage']
            newMe['Hit Points'] += spells[s]['heal']
            newMe['Armor'] += spells[s]['armor']
            newMe['Mana'] += spells[s]['mana']
        t -= 1
        if t > 0:
            newSpells.append((s, t))
        else:
            newSpells.append((s, -1))

    if newBoss['Hit Points'] <= 0:
        if manaUsed < minManaUsed:
            minManaUsed = manaUsed
            print manaUsed
            printSpells(activeSpells)
        return True

    if manaUsed > minManaUsed:
            return False

    if meTurn:
        for s1 in range(len(spells)):
            spell = spells[s1]
            isSpellUsed = False
            for (s2, t2) in newSpells:
                if s1 == s2 and t2 >= 0:
                    isSpellUsed = True
                    break
            if spell['costs'] <= newMe['Mana'] and not isSpellUsed:
                s = deepcopy(newSpells)
                s.append((s1, spell['turns']))
                m = deepcopy(newMe)
                m['Mana'] -= spell['costs']
                sim(m, newBoss, s, False, manaUsed+spell['costs'])
    else:
        if newMe['Armor'] >= boss['Damage']:
            newMe['Hit Points'] -= 1
        else:
            newMe['Hit Points'] += newMe['Armor']
            newMe['Hit Points'] -= newBoss['Damage']
        if newMe['Hit Points'] > 0:
            sim(newMe, newBoss, newSpells, True, manaUsed)
        else:
            return False


def main():
    for i in range(len(spells)):
        for k in ['costs', 'damage', 'armor', 'heal', 'mana', 'turns']:
            if k not in spells[i].keys():
                spells[i][k] = 0

    boss = dict()
    me = {
        'Hit Points': 50,
        'Mana': 500
    }

    for line in read_file('input'):
        match = re.match(RE_INPUT, line)
        boss[match.group(1)] = int(match.group(2))

    sim(me, boss, [], True, 0)
    print minManaUsed

if __name__ == "__main__":
    main()
