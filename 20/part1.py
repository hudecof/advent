#!/usr/bin/python

from math import  ceil, sqrt

def get_present_for_house(houseNumber):
    result = 0
#    print "house: %d" % houseNumber
    for x in range(int(sqrt(houseNumber))):
        elf = x+1
        if houseNumber % (elf) == 0:
#            print "elf: %d, %d" % (elf, houseNumber/elf)
            result += (elf)*10
            if elf != houseNumber / elf:
                result += (houseNumber / elf) * 10
    return result


def main():

    input = 36000000
    houseNumber = int(sqrt(input))
    while True:
        giftNumber = get_present_for_house(houseNumber)
        print "house: %d, gifts: %d" % (houseNumber, giftNumber)
        if giftNumber >= input:
            break
        houseNumber += 1
    print houseNumber


if __name__ == "__main__":
    main()
