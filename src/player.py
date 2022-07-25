import enum as e

class PlayerData:

    def __init__(self, sign, marker):
        self.sign   = sign
        self.marker = marker

class Player(e.Enum):

    MAX = PlayerData(sign=+1, marker='x')
    MIN = PlayerData(sign=-1, marker='o')

    def __str__(self):
        return f'{self.value.marker}'

    def __int__(self):
        return self.value.sign

    def __mul__(self, value):
        return self.value.sign * value

    def next(self):
        return Player.MAX if self == Player.MIN else Player.MIN
