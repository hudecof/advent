#!/usr/bin/python

import re

RE_MATCH_LONGEST = re.compile(r'(.)(\1*)')


def lookAndSay(sequence):
    pos = 0
    result = ""
    while pos < len(sequence):
        match = re.match(RE_MATCH_LONGEST, sequence[pos:])
        pos += len(match.group(2)) + 1
        result = "%s%d%s" % (result, len(match.group(2))+1, match.group(1))
    return result


def main():
    input = "1113222113"
    for x in range(0, 40):
        input = lookAndSay(input)

    print len(input)

if __name__ == "__main__":
    main()
