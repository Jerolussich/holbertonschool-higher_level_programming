#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argument_number = len(sys.argv)
    counter = 1
    sum = 0

    for counter in range(1, argument_number):
        sum += int(sys.argv[counter])
    print(sum)
