import numpy as np
import itertools as it
import functools as f

from utils import Player

class TicTacToeBoard:

    default = '-'

    def __init__(self):
        self.board = np.full((3, 3), None, dtype=Player)

    def __str__(self):
        return '\n'.join([' '.join([str(pos) if pos is not None else self.default for pos in row]) for row in self.board])

    def __hash__(self):
        return int.from_bytes(str.encode(''.join([str(pos) if pos is not None else self.default for pos in self.board.flatten()])), byteorder='little')

    def set(self, coordinates, player):
        (x, y) = coordinates
        self.board[y][x] = player

    def get(self, coordinates):
        (x, y) = coordinates
        return self.board[y][x]

    def copy(self):
        new_board = TicTacToeBoard()
        new_board.board = self.board.copy()
        return new_board

    def evaluate(self):
        lines = [
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0))
        ]

        for (a_prime, b_prime, c_prime) in lines:
            positions = [self.get(a_prime), self.get(b_prime), self.get(c_prime)]
            if all([p is not None for p in positions]) and len(set(positions)) == 1:
                return positions[0] * 1

        score = 0
        for (a_prime, b_prime, c_prime) in lines:
            positions = [self.get(a_prime), self.get(b_prime), self.get(c_prime)]
            if all([p is not None for p in positions]) and len(set(positions)) == 2:
                blocking = [p for p in positions if positions.count(p) == 1][0]
                score += blocking * 0.05

        return score

    def children(self, player):
        children = []
        for coordinates in it.product(range(3), range(3)):
            if self.get(coordinates) is None:
                child = self.copy()
                child.set(coordinates, player)
                children.append(child)
        return children

