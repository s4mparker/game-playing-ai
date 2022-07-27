import enum as e
import random as r

class NodeType(e.Enum):

    TRANSPOSITION = 0
    MAX_DEPTH     = 1
    TERMINAL      = 2
    NORMAL        = 3

    def __str__(self):
        return f'{self.name}'

class Node:

    """ Constructor """
    def __init__(self, state=None, value=0, flag=None):
        self.state      = state
        self.value      = value
        self.flag       = flag
        self.children   = []
        self.randid     = r.randint(1, 1000)

    """ State property """
    state = property(fget=lambda o: o._state, fset=lambda o, v: o.__setattr__('_state', v))
    """ Value property """
    value = property(fget=lambda o: o._value, fset=lambda o, v: o.__setattr__('_value', v))
    """ Flag property """
    @property
    def flag(self):
        return self._flag
    @flag.setter
    def flag(self, value):
        if value is not None and type(value) != NodeType:
            raise TypeError('expected a NodeType parameter')
        else:
            self._flag = value
    """ Children property """
    children = property(fget=lambda o: o._children, fset=lambda o, v: o.__setattr__('_children', v))

    """ Dunder methods """
    def __str__(self):
        return f'\nNode {self.randid} ({self.value}, {self.flag}, {len(self.children)})\n{"="*10}\n{str(self.state)}\n'

    def __len__(self):
        return sum([len(child) for child in self.children]) + 1

    def __iter__(self):
        return iter(self.children)

    """ Children methods """
    def addChild(self, child):
        if type(child) is not Node:
            raise TypeError('expected a Node type')
        else:
            self._children.append(child)

    def addChildren(self, *children):
        if any([type(child) is not Node for child in self._children]):
            raise TypeError('expected a list of Node types')
        else:
            self._children.extend(children)
