from enum import Enum
from utils import BasicNode

__all__ = ['Flag', 'Node']

class Flag(Enum):
    STANDARD = 0
    TERMINAL = 1
    TRANSPOSITION = 2
    DEPTH = 3

class Node(BasicNode):

    def __init__(self, **kwargs):
        self.state = kwargs.pop('state', None)
        self.value = kwargs.pop('value', 0)
        self.flag  = kwargs.pop('flag', None)
        super().__init__(**kwargs)

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        if value is None or type(value) is Flag:
            self._flag = value
        else:
            raise TypeError('expected a Flag')
