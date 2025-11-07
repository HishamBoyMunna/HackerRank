#!/bin/env python3.13
# /prepare/python/strings/AlphabetRangoli
#
def print_rangoli(size):
    # your code goes here
    a_floor = 96
    a_ceil = 97 + size
    line_no = size + (size - 1)
    middle = line_no // 2 + 1
    line_width = size * 2 + (size - 1) * 2 - 1
    lis = [chr(x) for x in range(97 + (size - 1), 97 - 1, -1)]

    def make_string_upper(num):
        string = ""
        for x in range(1, num + 1):
            string += lis[x - 1] + "-"
        for x in range(num - 1, 0, -1):
            string += lis[x - 1] + "-"
        string = string[0 : len(string) - 1]
        print(string.center(line_width, "-"))

    for line in range(1, line_no + 1):
        if line < middle:
            make_string_upper(line)
        elif line == middle:
            make_string_upper(line)
        else:
            make_string_upper(line - 2 * (line - middle))
