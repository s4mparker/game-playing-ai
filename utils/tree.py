from random import choices
from string import ascii_lowercase

class BasicNode:

    def __init__(self, parent=None):
        self.id       = ''.join(choices(ascii_lowercase, k=5))
        self.parent   = parent
        self.children = []
        
    def __len__(self):
        return len(self.children)

    def __str__(self):
        return f'Node: {self.id}'

    def __iter__(self):
        return iter(self.children)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node is None or issubclass(type(node), BasicNode):
            self._parent = node
        else:
            raise TypeError('expected a BasicNode subclass')

    @property
    def depth(self):
        if self.parent:
            return self.parent.depth + 1
        else:
            return 0

    @property
    def size(self):
        return sum([child.size for child in self.children]) + 1

    def addChild(self, node):
        if issubclass(type(node), BasicNode):
            node.parent = self
            self.children.append(node)
        else:
            raise TypeError('expected a BasicNode subclass')

def dfs(node, func):
    func(node)
    for child in node.children:
        dfs(child, func)

def bfs(node, func):
    queue = [node]
    while len(queue) > 0:
        item = queue.pop(0)
        func(item)
        queue.extend(item.children)