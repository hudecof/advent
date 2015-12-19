#!/usr/bin/python

import json
from pprint import pprint

def traverse_structructure(data):

    result = []

    if type(data) is list:
        for item in data:
            for value in traverse_structructure(item):
                if value is None:
                    value = 0
                yield value

    if type(data) is dict:
        sum = 0
        foundNone = False
        for key in data.keys():
            for value in traverse_structructure(data[key]):
                print "dict: %s" % value
                if value is None:
                    foundNone = True
                    value = 0
                sum += value
        if foundNone:
            sum = 0
        yield sum

    if type(data) is unicode:
        if data == 'red':
            yield None
        else:
            yield 0

    if type(data) is int:
        yield data


def main():
    with open("input") as data_file:
        input = json.load(data_file)

    sum = 0
    for value in traverse_structructure(input):
        if value is not None:
            sum += value

    print sum

if __name__ == "__main__":
    main()

