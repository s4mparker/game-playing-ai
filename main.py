from utils import Player, dfs, bfs
from minimax import Minimax
from games import TicTacToeBoard, Connect4Board

# board = TicTacToeBoard()
# print(board)

# m = Minimax.generate(board, Player.MAX, transpositions=False, alpha_beta=False, limit=2)

# func = lambda node : print(f'{" "*node.depth}{node}')
# bfs(m, func)
# print(f'Tree: {m.size}')

c = Connect4Board()
print(c, end='\n\n')


for child in c.children(Player.MAX):
    print(child, end='\n\n')