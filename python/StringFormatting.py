#!/bin/env python3.13
# /prepare/python/strings/StringFormatting


def print_formatted(number):
    # your code goes here
    leng = len(str(bin(number))) - 1
    for i in range(1, number + 1):
        binn = (str(bin(i))[2:]).rjust(leng, " ")
        hexn = (str(hex(i))[2:]).rjust(leng, " ").upper()
        octn = (str(oct(i))[2:]).rjust(leng, " ")

        print(str(i).rjust(leng - 1, " "), octn, hexn, binn, sep="")
