import numpy as np
from . import Player, TreeNode, Table

class Minimaxer:

    def __init__(self, state, player, **kwargs):
        use_transpositions  = kwargs.pop('use_transpositions', False)
        use_alphabeta       = kwargs.pop('use_alphabeta', False)
        limit               = kwargs.pop('limit', 5)

        self.transpositions = Table() if use_transpositions else None
        self.alphabeta      = use_alphabeta
        self.limit          = limit
        self.tree           = self.minimax(state, player)

    def minimax(self, state, player, depth=0, alpha=-1*np.Inf, beta=np.Inf):
        if self.transpositions is not None and state in self.transpositions:
            return TreeNode(data=self.transpositions[state])

        if depth >= self.limit:
            return TreeNode(data=state.evaluate())

        children = state.children(player)
        if len(children) < 1:
            value = state.evaluate()
            if self.transpositions is not None and state not in self.transpositions:
                self.transpositions[state] = value
            return TreeNode(data=value)
        else:
            node = TreeNode(data=(player * np.Inf) * -1)
            next_player = player.next()

            for child in children:
                child_node = self.minimax(child, next_player, depth=depth+1, alpha=alpha, beta=beta)
                node.addChild(child=child_node)

                if player == Player.MAX:
                    if child_node.getData() > node.getData():
                        node.setData(child_node.getData())
                    if self.alphabeta:
                        alpha = max(alpha, node.getData())
                else:
                    if child_node.getData() < node.getData():
                        node.setData(child_node.getData())
                    if self.alphabeta:
                        beta = min(beta, node.getData())
                
                if self.alphabeta and beta <= alpha:
                    break
            
            if self.transpositions is not None and state not in self.transpositions:
                    self.transpositions[state] = node.getData()
            return node
