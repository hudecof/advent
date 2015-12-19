#!/usr/bin/python

import re

RE_PAIR = re.compile(r'(.)\1.*(.)\2')

def get_next_char(ch):
    i = ord(ch) + 1
    if i > 122:
        return (True, 'a')
    return (False, chr(i))


def get_next_password(passwd):

    result = ""
    copy = False
    overflow = None
    for pos in reversed(range(len(passwd))):
        if not copy:
            (overflow, ch) = get_next_char(passwd[pos])
            result = ch + result
            copy = not overflow
        else:
            result = passwd[pos] + result
    if overflow:
        result = 'a' + result
    return result

def check_password(passwd):

    if passwd.count('i') > 0:
        return False
    if passwd.count('l') > 0:
        return False
    if re.search(RE_PAIR, passwd) is None:
        return False

    for pos in range(len(passwd)-2):
        x1 = ord(passwd[pos])
        x2 = ord(passwd[pos+1])
        x3 = ord(passwd[pos+2])
        if (x1 +1 != x2):
            continue
        if (x2 +1 != x3):
            continue
        break
    else:
        return False

    return True


def main():
    input = 'vzbxkghb';
    while True:
        input = get_next_password(input)
        if check_password(input):
            break
    while True:
        input = get_next_password(input)
        if check_password(input):
            break
    print input

if __name__ == "__main__":
    main()
