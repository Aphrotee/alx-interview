#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 8964875675645357464
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
