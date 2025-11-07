#!/bin/env python3.13
# /prepare/python/strings/TextWrap

import textwrap


def wrap(string, max_width):
    wrapped_string = ""
    if len(string) % max_width == 0:
        line_number = len(string) // max_width
    else:
        line_number = len(string) // max_width + 1
    for i in range(line_number):
        line_block = string[i * 4 : i * 4 + 4]
        wrapped_string = wrapped_string + line_block + "\n"
    return wrapped_string


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
