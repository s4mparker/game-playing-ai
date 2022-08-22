import math as m
import numpy as np
from random import choice, seed

from mcts import Node
from utils import Player, dfs

__all__ = ['MCTS']

class MCTS:

    @classmethod
    def generate(cls, state, player, limit=5, c=0.2):
        root = Node(state=state)

        for iteration in range(1, limit+1):
            node, current_player = root, player

            # Selection
            while len(node) > 0:
                best = {'node': None, 'value': -1 * np.Inf}
                for child in node.children:
                    ucb1 = cls.ucb1(child, iteration, c)
                    if ucb1 > best['value']:
                        best = {'node': child, 'value': ucb1}
                node, current_player = best['node'], current_player.next

            # Expansion
            children = node.state.children(current_player)
            for child in children: 
                node.addChild(Node(state=child))
            if len(children) > 0:
                node, current_player = choice(node.children), current_player.next

            # Exploration
            state = node.state
            children = state.children(current_player)
            while len(children) > 0:
                state = choice(children)
                current_player = current_player.next
                children = state.children(current_player)
            value = state.evaluate()

            # Backpropogation
            node += value
            while node.parent is not None:
                node = node.parent
                node += value

        return root

    @staticmethod
    def ucb1(node, t, c):
        if node.visited > 0:
            value = node.value + c * m.sqrt(m.log(t) / node.visited)
            return value
        else:
            return np.Inf
