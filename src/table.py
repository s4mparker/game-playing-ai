
class Table(dict):

    def __init__(self, allow_overwriting=False, default_value=None):
        self.allow_overwriting = allow_overwriting
        self.default_value     = default_value
        super().__init__()

    def __getitem__(self, key):
        tkey = self.transform_key(key)
        if tkey in self.keys():
            return super().__getitem__(tkey)
        elif self.default_value:
            return self.default_value
        else:
            raise KeyError('key not found')
    
    def __setitem__(self, key, value):
        tkey = self.transform_key(key)
        if tkey not in self.keys() or self.allow_overwriting:
            super().__setitem__(tkey, value)
        else:
            raise ValueError('key already present')

    def __delitem__(self, key):
        tkey = self.transform_key(key)
        if tkey in self.keys():
            super().__delitem__(tkey)
        else:
            raise KeyError('key not found')

    def __str__(self):
        return '\n'.join([f'{k}: {v}' for (k, v) in self.items()])

    def __contains__(self, key):
        tkey = self.transform_key(key)
        return tkey in self.keys()

    def transform_key(self, key):
        return hash(key)
