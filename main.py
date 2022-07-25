from src import Minimaxer, Player
from games import TicTacToeBoard

game = TicTacToeBoard()
game.set((0, 1), Player.MAX)
game.set((1, 1), Player.MAX)
game.set((2, 1), Player.MAX)
print(game.evaluate())