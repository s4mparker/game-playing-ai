
class Table:

    def __init__(self, **kwargs):
        self.allow_overwriting = kwargs.pop('allow_overwriting', False)
        self.default_value     = kwargs.pop('default_value', None)
        self.mapping           = {}

    def __getitem__(self, key):
        key_prime = self.transform_key(key)
        if key_prime in self.mapping.keys():
            return self.mapping[key_prime]
        elif key_prime not in self.mapping and self.default_value:
            return self.default_value
        else:
            raise KeyError('missing key')

    def __setitem__(self, key, value):
        key_prime = self.transform_key(key)
        if key_prime not in self.mapping.keys():
            self.mapping[key_prime] = value
        elif key_prime in self.mapping.keys() and self.allow_overwriting:
            self.mapping[key_prime] = value
        else:
            raise ValueError('key already present')

    def __delitem__(self, key):
        key_prime = self.transform_key(key)
        if key_prime in self.mapping.keys():
            del self.mapping[key_prime]
        else:
            raise KeyError('missing key')

    def __iter__(self):
        return iter(self.mapping)

    def __len__(self):
        return len(self.mapping.keys())

    def __str__(self):
        return '\n'.join([f'{k}: {v}' for (k, v) in self.mapping.items()])

    def __contains__(self, key):
        key_prime = self.transform_key(key)
        return key_prime in list(self.mapping.keys())

    def transform_key(self, key):
        return hash(key)


