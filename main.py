from src import Minimaxer, Player, Table
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


m = Minimaxer(b, Player.MAX, limit=20, use_transpositions=True, use_alphabeta=True)
print(m.tree)
print(len(m.tree))
