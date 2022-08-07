import numpy as np

from utils import Player

class Connect4Board:

    default = '-'

    def __init__(self, width=4, height=4):
        self.board = np.full((height, width), None, dtype=Player)

    def __str__(self):
        return '\n'.join([' '.join([str(pos) if pos is not None else self.default for pos in row]) for row in self.board])

    def __hash__(self):
        return int.from_bytes(str.encode(''.join(pos if pos is not None else self.default for pos in self.board.flatten())), byteorder='little')

    def set(self, coordinates, player):
        (x, y) = coordinates
        self.board[y][x] = player

    def get(self, coordinates):
        (x, y) = coordinates
        return self.board[y][x]

    def copy(self):
        shape = self.board.shape
        new_board = Connect4Board(width=shape[1], height=shape[0])
        new_board.board = self.board.copy()
        return new_board

    def evaluate(self):
        pass

    def children(self, player):
        children = []
        for column in range(self.board.shape[1]):
            for row in range(self.board.shape[0]):
                if self.get((column, row)) is not None:
                    if row > 0:
                        child = self.copy()
                        child.set((column, row-1), player)
                        children.append(child)
                    break
                elif row == self.board.shape[0] - 1:
                    child = self.copy()
                    child.set((column, row), player)
                    children.append(child)
                    break

        return children


