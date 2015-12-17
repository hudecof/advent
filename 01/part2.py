#!/usr/bin/python


def read_file(filename, chunk=1024):
    file = open(filename, 'r')
    while True:
        line = file.read(chunk)
        if not line:
            break
        yield line


def main():
    floor = 0
    pos = 1
    for line in read_file('input', 1):
        up = line.count('(')
        down = line.count(')')
        floor = floor + up - down
        if floor == -1:
            break
        pos = pos + 1

    print pos

if __name__ == "__main__":
    main()
