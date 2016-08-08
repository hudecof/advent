#!/usr/bin/python

mQ = None
mC = None

def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def calculate_qe(packages, used):

    if sum(used) == 0:
        return None

    result = 1
    for i in range(len(packages)):
        if used[i]:
            result *= packages[i]
    return result


def calculate_weight(packages, used):
    if sum(used) == 0:
        return None

    result = 0
    for i in range(len(packages)):
        result += packages[i]*used[i]
    return result


def find_group_packags(packagesList, packagesUsed,  maxPackages, packagesWeight, pos):

    global mC
    global mQ

    if sum(packagesUsed) > maxPackages:
        return

    weight = calculate_weight(packagesList, packagesUsed)

    if weight > packagesWeight:
        return

    if mC is not None and sum(packagesUsed) > mC:
        return
    if mQ is not None and calculate_qe(packagesList, packagesUsed) > mQ:
        return

    if pos >= len(packagesList):
        if weight == packagesWeight:
            qe = calculate_qe(packagesList, packagesUsed)
            yield (sum(packagesUsed), qe)
        return

    for i in range(2):
        packagesUsed[pos] = i
        for (c, q) in find_group_packags(packagesList, packagesUsed, maxPackages, packagesWeight, pos+1):
            if mC is None:
                mC = c
            if c is not None:
                mC = min (c, mC)
            if mQ is None:
                mQ = q
            if q is not None:
                mQ = min(q, mQ)
            yield (c, q)
    packagesUsed[pos] = 0

def main():
    weights = []
    packagesUsed = []
    for line in read_file('input'):
        weights.append(int(line))
        packagesUsed.append(0)

    weights_sum = sum(weights)
    group_weight = int(weights_sum / 4)
    group_1_max_packages = int(len(weights) / 4)

    for (c, q) in find_group_packags(weights, packagesUsed, group_1_max_packages, group_weight, 0):
        print "%010d %d" % (c, q)

if __name__ == "__main__":
    main()
