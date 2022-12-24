#!/usr/bin/python3
"""
This module provides the pascal triangle function.
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """

    subList = [1]
    result = []
    while n > 0:
        result.append(subList)
        helperList = subList.copy()
        prevNum = 0
        subList = []
        for nextNum in helperList:
            subList.append(prevNum + nextNum)
            prevNum = nextNum
        subList.append(1)
        n -= 1

    return result
