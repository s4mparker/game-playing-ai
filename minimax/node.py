from enum import Enum
from utils import nodify

__all__ = ['Flag', 'Node']

class Flag(Enum):
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