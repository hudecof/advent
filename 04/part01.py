#!/usr/bin/python

import hashlib
import re


def main():
    number = 0
    input = "yzbqklnj"

    while True:
        s = "%s%d" % (input, number)
        m = hashlib.md5()
        m.update(s)
        h = m.hexdigest()
        if re.match(r'^(0){5}', h):
            print number
            print h
            break
        number = number + 1

if __name__ == "__main__":
    main()
