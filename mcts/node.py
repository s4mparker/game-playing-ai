from utils import BasicNode

__all__ = ['Node']

class Node(BasicNode):

    def __init__(self, **kwargs):
        self.state   = kwargs.pop('state', None)
        self.visited = 0
        self.values  = []
        super().__init__(**kwargs)
    
    @property
    def value(self):
        if len(self.values) < 1:
            return 0
        return sum(self.values) / len(self.values)

    def __add__(self, value):
        self.values.append(value)
        self.visited += 1
        return self

    def __iadd__(self, value):
        return self + value