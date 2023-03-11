#!/usr/bin/python3

"""
This module provides the function `isWinner`
"""


def isWinner(x, nums):
    """
    This function plays the primegame between
    two players and returns the winner
    """
    if x is None or nums is None:
        return
    if not isinstance(x, int):
        return
    if type(nums) != list:
        return
    if len(nums) != x:
        return

    class PrimeGame:
        """ A class for playaing Prime game """
        def __init__(self, X, Nums):
            self.x = X
            self.nums = Nums
            self.Ben = 0
            self.Maria = 0
            self.roundList = []

        @staticmethod
        def checkPrime(k):
            """
            checks if the input x is a prime number
            """
            if k == 1:
                return False
            for i in range(2, int(k / 2) + 1):
                if k % i == 0:
                    return False
            return True

        def play(self):
            """
            Starts the gameplay to determine the winner
            """
            for n in self.nums:
                self.roundList = [i for i in range(1, n + 1)]
                self.roundList = list(filter(self.checkPrime, self.roundList))
                numOfPrime = len(self.roundList)
                if numOfPrime % 2 == 0:
                    self.Ben += 1
                else:
                    self.Maria += 1

    game = PrimeGame(x, nums)
    game.play()

    if game.Ben > game.Maria:
        return 'Ben'
    elif game.Maria > game.Ben:
        return 'Maria'
    else:
        return
