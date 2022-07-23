import enum as e
import numpy as np

class ResultType(e.Enum):

    HEURISTIC = 0
    LEAF_NODE = 1
    NORMAL = 2

class Result:
    
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.children = []

    def __str__(self):
        return f'{self.type.name} {self.value}: {str(self.children)}'

    def updateValue(self, value):
        self.value = value

    def addChild(self, child):
        self.children.append(child)

class Minimaxer:

    def __init__(self, node, maximising, limit=5):
        self.limit = limit
        self.tree = self.minimax(node=node, maximising=maximising)

    def minimax(self, node, maximising, depth=0):
        if depth >= self.limit:
            return Result(ResultType.HEURISTIC, node.evaluate())

        children = node.children(maximising)
        if len(children) < 1:
            return Result(ResultType.LEAF_NODE, node.evaluate())

        initial = np.NINF if maximising else np.Inf
        optimal = Result(ResultType.NORMAL, initial)

        for child in children:
            result = self.minimax(child, not maximising, depth=depth+1)
            print(f'    Result: {result.value}\n{child}')
            optimal.addChild(result)

            if maximising and result.value > optimal.value:
                optimal.updateValue(result.value)
            elif not maximising and result.value < optimal.value:
                optimal.updateValue(result.value)
        
        return optimal
