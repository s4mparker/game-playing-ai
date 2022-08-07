import numpy as np
import enum as e
import time as t

from utils import Player, Table, nodify

class NodeFlag(e.Enum):
    STANDARD = 0
    TERMINAL = 1
    TRANSPOSITION = 2
    DEPTH = 3

@nodify
class Node:

    state = property(lambda o: getattr(o, '_state'), lambda o, v: setattr(o, '_state', v))
    value = property(lambda o: getattr(o, '_value'), lambda o, v: setattr(o, '_value', v))
    flag  = property(lambda o: getattr(o, '_flag'), lambda o, v: setattr(o, '_flag', v))

    def __init__(self, **kwargs):
        state = kwargs.pop('state', None)
        value = kwargs.pop('value', 0)
        flag  = kwargs.pop('flag', None)

class Minimaxer:

    def __init__(self, state, player, **kwargs):
        use_transpositions  = kwargs.pop('use_transpositions', False)
        use_alphabeta       = kwargs.pop('use_alphabeta', False)
        limit               = kwargs.pop('limit', 5)
        verbose             = kwargs.pop('verbose', 0)

        self._transpositions = Table() if use_transpositions else None
        self._alphabeta      = use_alphabeta
        self._limit          = limit
        self._verbose        = verbose

        self.generateTree(state, player)

    def generateTree(self, state, player):
        start = t.time()
        self._tree = self.minimax(state, player)
        end = t.time()

        if self._verbose >= 1:
            print(f'Generated a tree containing {len(self._tree)} nodes in {round(end-start, 2)}s')

    def minimax(self, state, player, depth=0, alpha=-1*np.Inf, beta=np.Inf):
        node        = Node()
        node.state  = state
        children    = state.children(player)

        if bool(self._transpositions) and state in self._transpositions:
            node.value = self._transpositions[state]
            node.flag  = NodeFlag.TRANSPOSITION
        elif depth >= self._limit:
            node.value = state.evaluate()
            node.flag  = NodeFlag.DEPTH
        elif len(children) < 1:
            node.value = state.evaluate()
            node.flag  = NodeFlag.TERMINAL
        else:
            node.value = (player * np.Inf) * -1
            node.flag  = NodeFlag.STANDARD

            for child in children:
                childnode = self.minimax(child, player.next, depth+1, alpha, beta)
                node.addChild(childnode)

                if player == Player.MAX and childnode.value > node.value:
                    node.value = childnode.value
                elif player == Player.MIN and childnode.value < node.value:
                    node.value = childnode.value

                if self._alphabeta:
                    alpha = max(alpha, node.value) if player == Player.MAX else alpha
                    beta  = min(beta, node.value) if player == Player.MIN else beta
                    if beta <= alpha:
                        break

        if node.flag in [NodeFlag.TERMINAL, NodeFlag.STANDARD] and bool(self._transpositions):
            self._transpositions[state] = node.value
        
        return node
