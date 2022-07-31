import enum as e
import random as r

def nodify(cls):

    class Node(cls):
        parent   = property(lambda o: getattr(o, '_parent'), lambda o, v: setattr(o, '_parent', v))
        children = property(lambda o: getattr(o, '_children'), lambda o, v: setattr(o, '_children', v))
        
        def __init__(self, parent=None, **kwargs):
            if parent : parent.addChild(self)
            self.parent   = parent
            self.children = []
            self.nodeid   = r.randint(1, 1e10)
            cls.__init__(self, **kwargs)

        def addChild(self, node):
            self.children.append(node)
        
        def __len__(self):
            return len(self.children)
        
        def __str__(self):
            return f'{self.nodeid} (children: {len(self)})'

        def __iter__(self):
            return iter(self.children)

    return Node
    
@nodify
class Data:

    x = property(lambda o: getattr(o, '_x'), lambda o, v: setattr(o, '_x', v))

    def __init__(self, *args, **kwargs):
        self.x = 10


if __name__ == '__main__':
    d = Data()
    print(str(d))