#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]) - {0}

    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if 0 <= boxIdx < n and boxIdx not in seen_boxes:
            unseen_boxes.update(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    return n == len(seen_boxes)
