import numpy as np

from minimax import Node, Flag
from utils import Player, Table

__all__ = ['Minimax']

class Minimax:

    @classmethod
    def generate(cls, state, player, transpositions=True, alpha_beta=True, limit=None):
        return cls.minimax(
            state          = state,
            player         = player,
            transpositions = Table() if transpositions else None,
            depth          = 0,
            limit          = limit if limit is not None else np.Inf,
            alpha          = -1*np.Inf if alpha_beta else None,
            beta           = +1*np.Inf if alpha_beta else None
        )

    @classmethod
    def minimax(cls, state, player, transpositions, depth, limit, alpha, beta):
        node        = Node()
        node.state = state

        if bool(transpositions) and state in transpositions:
            node.value, node.flag = transpositions[state], Flag.TRANSPOSITION
        elif depth >= limit:
            node.value, node.flag = state.evaluate(), Flag.DEPTH
        else:
            children = state.children(player)

            if len(children) < 1:
                node.value, node.flag = state.evaluate(), Flag.TERMINAL
            else:
                node.value, node.flag = -1 * (player * np.Inf), Flag.STANDARD

                for child in children:
                    subnode = cls.minimax(
                        state          = child,
                        player         = player.next,
                        transpositions = transpositions,
                        depth          = depth + 1,
                        limit          = limit,
                        alpha          = alpha,
                        beta           = beta
                    )
                    node.addChild(subnode)

                    if player == Player.MAX and subnode.value > node.value:
                        node.value = subnode.value
                    if player == Player.MIN and subnode.value < node.value:
                        node.value = subnode.value

                    if alpha is not None and beta is not None:
                        alpha = max(alpha, node.value) if player == Player.MAX else alpha
                        beta  = min(beta,  node.value) if player == Player.MIN else beta
                        if beta <= alpha : break
            
        if node.flag in [Flag.TERMINAL, Flag.STANDARD] and bool(transpositions) and state not in transpositions:
            transpositions[state] = node.value

        return node
