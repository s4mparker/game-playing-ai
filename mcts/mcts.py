import math as m
import numpy as np
from random import choice, seed

from mcts import Node
from utils import Player, dfs

__all__ = ['MCTS']

class MCTS:

    @classmethod
    def generate(cls, state, player, limit=10, c=0.2):
        seed = 100
        root = Node(state=state)

        for iteration in range(1, limit+1):
            node, cplayer = cls.selection(root, player, iteration)
            node, cplayer = cls.expansion(node, cplayer)
            value         = cls.exploration(node, cplayer)
            cls.backpropogation(node, value)

        return root

    @classmethod
    def selection(cls, node, player, iteration):
        while len(node) > 0:
            node = choice(node.children)
            player = player.next
        return node, player

    @classmethod
    def expansion(cls, node, player):
        children = node.state.children(player)

        if len(children) > 0:
            for child in children:
                n = Node(state=child)
                node.addChild(n)
            node   = choice(node.children)
            player = player.next

        return node, player

    @classmethod
    def exploration(cls, node, player):
        state    = node.state
        children = state.children(player)

        while len(children) > 0:
            state = choice(children)
            children = state.children(player)
            player = player.next

        return state.evaluate()

    @classmethod
    def backpropogation(cls, node, value):
        node += value
        while node.parent is not None:
            node = node.parent
            node += value

    @staticmethod
    def ucb1(node, t, c):
        x = 100
        if node.visited > 0:
            x = m.sqrt(m.log(t) / node.visited)
        return node.value + (c * x)
