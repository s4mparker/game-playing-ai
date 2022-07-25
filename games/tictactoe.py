import numpy as np
import copy as cp
import itertools as it
import functools as f

from src import Player

class TicTacToeBoard:

    default = '-'

    def __init__(self, board=None):
        if board is not None:
            self.board = board.copy()
        else:
            self.board = np.full((3, 3), None, dtype=Player)

    def __str__(self):
        return '\n'.join([' '.join([str(pos) if pos is not None else self.default for pos in row]) for row in self.board])

    def __hash__(self):
        subhash = lambda board: int.from_bytes(str.encode(''.join([str(pos) if pos is not None else self.default for pos in board.flatten()])), byteorder='little')
        components = sorted([subhash(np.rot90(self.board, k=angle)) for angle in range(4)])
        hash = f.reduce(lambda x, y: x^y+x+y, components)
        return hash

    def set(self, coordinates, player):
        (x, y) = coordinates
        self.board[y][x] = player

    def get(self, coordinates):
        (x, y) = coordinates
        return self.board[y][x]

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
            a, b, c = self.get(a_prime), self.get(b_prime), self.get(c_prime)
            if a is not None and b is not None and c is not None:
                if a == b and b == c:
                    return a * np.Inf
                else:
                    blocking = [player for player in [a, b, c] if [a, b, c].count(player) == 1][0]
                    return blocking * 100

        full_positions = [player is not None for player in self.board.flatten()]
        if all(full_positions):
            return 0
        elif any(full_positions):
            return sum([int(player) for player in self.board.flatten() if player is not None])
        else:
            return 0

    def children(self, player):
        children = []
        for coordinates in it.product(range(3), range(3)):
            if self.get(coordinates) is None:
                child = TicTacToeBoard(board=self.board)
                child.set(coordinates, player)
                children.append(child)
        return children
