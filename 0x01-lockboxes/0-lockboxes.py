#!/usr/bin/python3

"""
This modeule supplies the function `canUnlockAll` which
analyses a list of lockboxes
"""


def checkBox(boxes, currentBox, register):
    """
    this function checks and unlocks other locked boxes
    """
    # analyses each key in a current box and it's corresponding box
    for key in currentBox:
        if key >= len(boxes):
            # if the current key has no box in the list of boxes
            # the loop skips that key
            continue
        # checks if the box corresponding to this
        # current key is locked or unlocked
        if not register[key]:
            # if the box is locked, it is unlocked and entered
            # to be further analysed
            register[key] = True
            # updates the register with the state of the newly unlocked boxes
            register = checkBox(boxes, boxes[key], register)
    # returns the updated register
    return register


def canUnlockAll(boxes):
    """
    This function checks is all boxes in a list of
    locked boxes can be unlocked.
    """
    # Create a True/False register representing the Locked/Unlocked
    # state of each box
    register = [False for lowestFactor in range(len(boxes))]
    # the first box is always open
    register[0] = True
    if len(boxes[0]) == 0:
        # if the first box has no keys, then no other box can be unlocked
        return False
    # updates the register with the state of the newly unlocked boxes
    register = checkBox(boxes, boxes[0], register)
    # checks if all the values in the register are true(unlocked)
    # and returns True if they are, otherwise False
    return all(register)
