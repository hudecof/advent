#!/usr/bin/python


def read_file(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        yield line.rstrip()


def getMemorySize(line):
    count = 0
    pos = 0
    while pos < len(line):
        if line[pos] != '\\':
            pos += 1
            count += 1
        elif line[pos+1] == '\\':
            pos += 2
            count += 1
        elif line[pos+1] == '"':
            pos += 2
            count += 1
        elif line[pos+1] == 'x':
            pos += 4
            count += 1
        else:
            print "chyba"
    return count


def main():

    numCode = 0
    numMem = 0
    for line in read_file('input'):
        numCode = numCode + len(line)
        numMem = numMem + getMemorySize(line) - 2
        print line

    print numCode
    print numMem
    print numCode - numMem

if __name__ == "__main__":
    main()
