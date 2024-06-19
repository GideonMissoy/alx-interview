#!/usr/bin/python3
"""determines if the boxes can be opened"""

def canUnlockAll(boxes):

    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    keys = [0]
    for y in keys:
        for k in boxes[y]:
            if k not in keys and k != y and k< len(boxes) and k != 0:
                keys.append(k)
    if len(keys) == len(boxes):
        return True
    else:
        return False
