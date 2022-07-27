import enum as e

class Player(e.Enum):

    MAX = {'sign': +1, 'marker': 'o'}
    MIN = {'sign': -1, 'marker': 'x'}

    def __str__(self):
        return f'{self.marker}'

    def __int__(self):
        return self.sign

    def __mul__(self, value):
        return self.sign * value

    @property
    def sign(self):
        return self.value['sign']

    @property
    def marker(self):
        return self.value['marker']

    @property
    def next(self):
        return Player.MAX if self == Player.MIN else Player.MIN
