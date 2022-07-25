import numpy as np
from . import Player, TreeNode

class Minimaxer:

    def __init__(self, state, player, limit=5):
        self.limit = limit
        self.result = self.minimax(state, player)

    def minimax(self, state, player, depth=0):
        if depth >= self.limit:
            return state.evaluate()

        children = state.children(player)
        if len(children) < 1:
            return state.evaluate()

        optimal = (player * np.Inf) * -1
        next_player = player.next()
        for child in children:
            child_value = self.minimax(child, next_player, depth=depth-1)
            if player == Player.MAX and child_value > optimal:
                optimal = child_value
            elif player == Player.MIN and child_value < optimal:
                optimal = child_value

        return optimal

