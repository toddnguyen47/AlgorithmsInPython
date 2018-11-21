class Tree:
    def __init__(self):
        raise NotImplementedError

    def insert(self, node_input, key, value):
        raise NotImplementedError

    def getValue(self, key):
        raise NotImplementedError

    def printTree(self):
        raise NotImplementedError


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = None


    def __str__(self):
        s = "Key: " + str(self.key) + ", Value: " + str(self.value) + ", Height: " + str(self.height)
        return s
