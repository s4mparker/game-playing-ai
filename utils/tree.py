import random as r
import string as s

def nodify(cls):

    class Node(cls):
        parent   = property(lambda o: getattr(o, '_parent'), lambda o, v: setattr(o, '_parent', v))
        children = property(lambda o: getattr(o, '_children'), lambda o, v: setattr(o, '_children', v))
        
        def __init__(self, parent=None, **kwargs):
            self.parent = parent
            self.children = []
            self.nodeid   = ''.join(r.choices(s.ascii_letters, k=5))
            cls.__init__(self, **kwargs)

        def addChild(self, node):
            if node.parent is not self : node.parent = self
            self.children.append(node)
        
        def __len__(self):
            return len(self.children)
        
        def __str__(self):
            return f'{self.nodeid} (children: {len(self)}, depth: {self.depth})'

        def __iter__(self):
            return iter(self.children)

        @property
        def depth(self):
            if self.parent:
                return self.parent.depth + 1
            else:
                return 0

        @property
        def size(self):
            return sum([child.size for child in self.children]) + 1

    return Node

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