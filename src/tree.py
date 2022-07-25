class TreeNode:

    def __init__(self, data=None):
        self.data       = data
        self.children   = []

    def __str__(self):
        return f'Node: {str(self.data)}'

    def __len__(self):
        nodes = []
        self.breadth_first_traversal(lambda item: nodes.append(item))
        return len(nodes)

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def addChild(self, child):
        self.children.append(child)

    def breadth_first_traversal(self, func):
        queue = [self]
        while len(queue) > 0:
            item = queue.pop(0)
            func(item)
            queue.extend(item.children)

    def depth_first_traversal(self, func):
        func(self)
        for child in self.children:
            child.depth_first_traversal(func)
