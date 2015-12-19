#!/usr/bin/python

import re

RE_TICKER = re.compile(r'^\s*(.*): (\d+)$')
RE_SUE = re.compile(r'Sue (\d+): (.*)')


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def main():

    ticker_type = dict()
    for line in read_file('ticker_type'):
        match = re.match(RE_TICKER, line)
        if not match:
            print "wrong input"
            print line
            break
        ticker_type[match.group(1)] = int(match.group(2))

    for line in read_file('input'):
        sue = dict()
        number = None
        match = re.match(RE_SUE, line)
        if not match:
            print "wrong input"
            print line
            break
        number = match.group(1)
        for token in match.group(2).split(','):
            match1 = re.match(RE_TICKER, token)
            sue[match1.group(1)] = int(match1.group(2))

        for k, v in ticker_type.iteritems():
            if k in sue:
                if sue[k] == v:
                    del sue[k]

        if len(sue.keys()) == 0:
            print number

if __name__ == "__main__":
    main()
