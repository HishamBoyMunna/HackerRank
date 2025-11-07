#!/bin/env python3.13
# /prepare/python/strings/TheMinionGame


def minion_game(string):
    # your code goes here
    n = len(string)
    S = string.upper()  # be robust to case
    vowels = set("AEIOU")

    kevin = 0  # vowel player
    stuart = 0  # consonant player

    for i, ch in enumerate(S):
        if ch in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
