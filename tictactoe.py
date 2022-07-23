import enum as e
import numpy as np
import copy as cp

from minimaxer import Minimaxer

class Player(e.Enum):

    MAXIMISING = {'char': 'x', 'value': 1}
    MINIMISING = {'char': 'o', 'value': -1}

    def __str__(self):
        return f'{self.value.get("char")}'

    def getValue(self, inf=False):
        value = self.value.get('value')
        if inf:
            if value > 0:
                return 100
            else:
                return -100
        else:
            return value

class TicTacToeBoard:

    default = '-'

    def __init__(self):
        self.board = np.full((3, 3), None, dtype=Player)

    def __str__(self):
        string = ''
        for i in range(3):
            for j in range(3):
                p = self.get((i, j))
                if type(p) is Player:
                    string += f' {p} '
                else:
                    string += f' {self.default} '
            string += '\n'

        return string
    
    def set(self, coordinates, player):
        (x, y) = coordinates
        self.board[y][x] = player

    def get(self, coordinates):
        (x, y) = coordinates
        return self.board[y][x]

    def evaluate(self):
        lines = [
            ((0, 0), (1, 0), (2, 0))
        ]

        for (c1, c2, c3) in lines:
            p1, p2, p3 = self.get(c1), self.get(c2), self.get(c3)

            if all(p is not None for p in [p1, p2, p3]):
                if p1 == p2 and p2 == p3:
                    return p1.getValue(inf=True)
                elif p1 != p2 and p2 == p3:
                    return p1.getValue() * 10
                elif p1 != p2 and p1 == p3:
                    return p2.getValue() * 10
                else:
                    return p3.getValue() * 10

        complete = all([p is not None for p in self.board.flatten()])
        if complete:
            return 0

        score = [p.getValue() for p in self.board.flatten() if p is not None]
        if len(score) < 1:
            return 0
        else:
            return score[0]

    def children(self, maximising):
        children = []
        player = Player.MAXIMISING if maximising else Player.MINIMISING

        for i in range(3):
            for j in range(3):
                if self.get((i, j)) is None:
                    child = cp.deepcopy(self)
                    child.set((i, j), player)
                    children.append(child)

        return children

if __name__ == '__main__':
    game = TicTacToeBoard()
    print(game)
    m = Minimaxer(game, True, limit=5)
    print(m.tree)




