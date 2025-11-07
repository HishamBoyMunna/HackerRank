#!/bin/env python3.13
# /prepare/python/strings/IfElse

import math
import os
import random
import re
import sys


def task(number: int) -> None:
    if number % 2 != 0:
        print("Weird")
    else:
        if number in range(2, 6):
            print("Not Weird")
        elif number in range(6, 21):
            print("Weird")
        elif number > 20:
            print("Not Weird")


if __name__ == "__main__":
    n = int(input().strip())
    task(n)
