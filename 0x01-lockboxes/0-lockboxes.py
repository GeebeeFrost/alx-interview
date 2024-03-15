#!/usr/bin/python3
"""This script contains the canUnlockAll function"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    opened_boxes = set()
    opened_boxes.add(0)
    key_stack = [0]

    while key_stack:
        box = key_stack.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in opened_boxes:
                key_stack.append(key)
                opened_boxes.add(key)

    return len(opened_boxes) == len(boxes)
