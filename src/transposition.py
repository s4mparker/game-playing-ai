
class TranspositionTable:

    def __init__(self):
        self.items = {}

    def put(self, item, value):
        key = hash(item)
        self.items[key] = value

    def get(self, item, default=None):
        key = hash(item)
        if key in self.items.keys():
            return self.items[key]
        else:
            raise KeyError()

    def __contains__(self, item):
        key = hash(item)
        return key in self.items.keys()

    def __str__(self):
        return '\n'.join([f'{k}: {v}' for (k, v) in self.items.items()])


