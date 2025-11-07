#!/bin/env python3.13
# /prepare/python/strings/DesignerDoorMat

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = input().split()
N = int(N)
M = int(M)

for line in range(N):
    if line == (N // 2):
        print("WELCOME".center(M, "-"))
    elif line < (N // 2):
        string = "." + "|.." * (line * 2) + "|."
        print(string.center(M, "-"))
    else:
        string = "." + "|.." * (((N - 1) - (line)) * 2) + "|."
        print(string.center(M, "-"))
