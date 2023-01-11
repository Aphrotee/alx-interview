#!/usr/bin/python3

'''
This module provides the function minOpertions
'''


def minOperations(n: int) -> int:
    '''
    This is a function that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
    '''
    if n < 1 or type(n) != int:
        return 0
    operations: int = 0
    while n >= 2:
        i: int = 2
        while i < n + 1:
            if n % i == 0:
                operations += i
                n /= i
                break
            i += 1
    return operations
