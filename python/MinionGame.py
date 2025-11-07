#!/bin/env python3.13
# /prepare/python/strings/TheMinionGame
#
def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    stuart_score = 0
    kevin_score = 0

    def get_kevin_score(string, score):
        length = len(string)
        kevin_score = score
        for i, alpha in enumerate(string):
            if alpha in vowels:
                # kevin_score += 1
                for j in range(1, len(string[i:length]) + 1):
                    if string[i : i + j] in string:
                        # print(string[i : i + j])
                        kevin_score += 1
        return kevin_score

    kevin_score = get_kevin_score(string, kevin_score)
    # print(kevin_score)

    def get_stuart_score(string, score):
        length = len(string)
        stuart_score = score
        for i, alpha in enumerate(string):
            if alpha not in vowels:
                # kevin_score += 1
                for j in range(1, len(string[i:length]) + 1):
                    if string[i : i + j] in string:
                        # print(string[i : i + j])
                        stuart_score += 1
        return stuart_score

    stuart_score = get_stuart_score(string, stuart_score)
    # print(stuart_score)

    if kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
