from src import Minimaxer
from utils import Player, dfs, bfs
from games import TicTacToeBoard

b = TicTacToeBoard()
p = Player.MAX

m = Minimaxer(b, p, limit=2)
bfs(m._tree, lambda x: print(f'{" "*x.depth}{str(x)}'))

