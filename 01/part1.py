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
    for line in read_file('input'):
        up = line.count('(')
        down = line.count(')')
        floor = floor + up - down

    print floor

if __name__ == "__main__":
    main()
