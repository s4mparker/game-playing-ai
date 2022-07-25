from src import Minimaxer, Player
from games import TicTacToeBoard

b = TicTacToeBoard()
b.set((0, 0), Player.MAX)
# b.set((1, 0), Player.MAX)
# b.set((0, 1), Player.MIN)
# b.set((1, 1), Player.MIN)
# b.set((2, 1), Player.MAX)
# b.set((1, 2), Player.MAX)
# b.set((0, 2), Player.MIN)
print(b)


m = Minimaxer(b, Player.MIN, limit=5, use_transposition=False)
print(m.tree)
print(len(m.tree))

