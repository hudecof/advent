#!/usr/bin/python

import json
from pprint import pprint

def traverse_structructure(data):

    result = []

    if type(data) is list:
        for item in data:
            for value in traverse_structructure(item):
                yield value

    if type(data) is dict:
        for key in data.keys():
            for value in traverse_structructure(data[key]):
                yield value

    if type(data) is unicode:
        yield 0

    if type(data) is int:
        yield data

#    print type(data)

def main():
    with open("input") as data_file:
        input = json.load(data_file)

    sum = 0
    for value in traverse_structructure(input):
        sum += value

    print sum

if __name__ == "__main__":
    main()

