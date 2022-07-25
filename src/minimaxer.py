import numpy as np
from . import Player, TreeNode, TranspositionTable

class Minimaxer:

    def __init__(self, state, player, limit=3, use_transposition=False):
        self.limit = limit
        self.transposition_table = TranspositionTable() if use_transposition else None
        self.tree = self.minimax(state, player)

    def minimax(self, state, player, depth=0):
        if self.transposition_table and state in self.transposition_table:
            return TreeNode(data=self.transposition_table.get(state))

        if depth >= self.limit:
            return TreeNode(data=state.evaluate())

        node = TreeNode(data=state.evaluate())
        children = state.children(player)

        if len(children) > 0:
            node.setData(data=(player * np.Inf) * -1)
            next_player = player.next()

            for child in children:
                result = self.minimax(child, next_player, depth=depth+1)
                node.addChild(result)

                if player == Player.MAX and result.getData() > node.getData():
                    node.setData(result.getData())
                elif player == Player.MIN and result.getData() < node.getData():
                   node.setData(result.getData())

        if self.transposition_table and state not in self.transposition_table:
            self.transposition_table.put(state, node.getData())

        return node

