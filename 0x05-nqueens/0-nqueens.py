#!/usr/bin/python3

"""
This module provides the n-queens bactracking algorithm
"""

import sys


class NQueens:
    """
    A class NQuuens for implementing
    the NQueens Backtracking Algorithm
    """

    dangerZones = {}
    queens = []

    def __init__(self, size):
        """ Initialize instance """
        self.rows, self.columns = size, size

    def get_danger_zones(self, position):
        """ Returns a list of all the positions a given queen can attack """
        row = position[0]
        col = position[1]
        dangerzones = []
        for i in range(self.rows):
            dangerzones.append((row, i))
            dangerzones.append((i, col))
        for i in range(1, self.rows):
            r = row - i
            c = col + i
            if r < 0 or c >= self.rows:
                break
            dangerzones.append((r, c))
        for i in range(1, self.rows):
            r = row + i
            c = col + i
            if r >= self.rows or c >= self.rows:
                break
            dangerzones.append((r, c))
        for i in range(1, self.rows):
            r = row - i
            c = col - i
            if r < 0 or c < 0:
                break
            dangerzones.append((r, c))
        for i in range(1, self.rows):
            r = row + i
            c = col - i
            if r >= self.rows or c < 0:
                break
            dangerzones.append((r, c))
        return list(set(dangerzones))

    def placeQueen(self, row, column):
        """ Places a queen on a position on the chessboard """
        position = (row, column)
        str_position = (str(row), str(column))
        self.queens.append(list(position))
        key = ','.join(str_position)
        self.dangerZones[key] = self.get_danger_zones(position)

    def removeQueen(self, row, column):
        """ Removes a quees from a position on the chessboard """
        position = (row, column)
        str_position = (str(row), str(column))
        key = ','.join(str_position)
        try:
            index = self.queens.index(list(position))
            self.queens.pop(index)
        except ValueError:
            print("Error! queen not found.")
        del self.dangerZones[key]

    def isValid(self, row, column):
        """ Checks if the current position isnt threatened by a queen """
        dangerzones = list(self.dangerZones.values())
        position = (row, column)
        for threats in dangerzones:
            if position in threats:
                return False
        return True

    def get_positions(self, row, column):
        """ Gets all queens' positions """
        r = row
        for c in range(column, self.columns):
            if self.isValid(r, c):
                self.placeQueen(r, c)
                if r + 1 < self.rows:
                    if self.get_positions(r + 1, 0):
                        return True
                    else:
                        self.removeQueen(r, c)
                        continue
                return True
        return False

    def get_all_positions(self):
        """ Starter funciont for get_positions """
        positions = []
        for i in range(self.columns):
            if self.get_positions(0, i):
                map(lambda x: list(x), self.queens)
                if self.queens not in positions:
                    print(self.queens)
                positions.append(self.queens)
                self.queens = []
                self.dangerZones = {}


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print('Usage: nqueens N')
        sys.exit(1)
    size = args[1]
    try:
        size = int(size)
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if size < 4:
        print('N must be at least 4')
        sys.exit(1)
    nqueens = NQueens(size)
    nqueens.get_all_positions()
