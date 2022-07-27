from src import Minimaxer, Player, Table
from games import TicTacToeBoard

b = TicTacToeBoard()

print(f'{b}\n\n')


m = Minimaxer(b, Player.MAX, limit=20, use_transpositions=False, use_alphabeta=True, verbose=1)

def dfs(tree, depth=0):
    print(f'{" "*depth}{tree}')
    for child in iter(tree):
        dfs(child, depth=depth+1)
    
# dfs(m._tree)

print(m._tree.value)
    