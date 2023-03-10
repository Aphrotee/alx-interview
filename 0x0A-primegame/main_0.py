#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [5, 1, 4])))
print("Winner: {}".format(isWinner(3, [12, 18, 1])))
print("Winner: {}".format(isWinner(2, [12, 1])))
