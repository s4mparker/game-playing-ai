from utils import Player, dfs, bfs
from minimax import Minimax
from mcts import MCTS
from games import TicTacToeBoard, Connect4Board

b = TicTacToeBoard()

# t = Minimax.generate(b, Player.MAX, transpositions=True, alpha_beta=True)
t = MCTS.generate(b, Player.MAX, c=0.5)

# for child in t:
#     print(f'{child.id}: {child.value}')

dfs(t, func=lambda x: print(f'{" " * x.depth}({x.depth} - {x.visited}) {x}'))
