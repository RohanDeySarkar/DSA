class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, arr):
        queue = [self]
        while len(queue) > 0:
            currentNode = queue.pop(0)
            arr.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
        return arr
