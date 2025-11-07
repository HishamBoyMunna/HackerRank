#!/bin/env python3.13
# /prepare/python/strings/StringValidators

if __name__ == "__main__":
    s = input()
    line1 = False
    line2 = False
    line3 = False
    line4 = False
    line5 = False

    for i in s:
        if i.isalnum():
            line1 = True
        if i.isalpha():
            line2 = True
        if i.isdigit():
            line3 = True
        if i.islower():
            line4 = True
        if i.isupper():
            line5 = True
    print(line1, line2, line3, line4, line5, sep="\n", end="\n")
