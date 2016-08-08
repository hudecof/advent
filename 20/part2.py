#!/usr/bin/python

from math import  ceil, sqrt

def get_present_for_house(houseNumber, delivered, max):
    result = 0
    for x in range(int(sqrt(houseNumber))):
        elf = x+1
        if houseNumber % (elf) == 0:
            if houseNumber <= elf*max:
                result += (elf)*delivered
            if houseNumber <= (houseNumber/elf)*max:
                if elf != houseNumber / elf:
                    result += (houseNumber/elf) * delivered
    return result


def main():

    input = 36000000
    houseNumber = int(sqrt(input))
    while True:
        giftNumber = get_present_for_house(houseNumber, 11, 50)
        print "house: %d, gifts: %d" % (houseNumber, giftNumber)
        if giftNumber >= input:
            break
        houseNumber += 1
    print houseNumber


if __name__ == "__main__":
    main()
