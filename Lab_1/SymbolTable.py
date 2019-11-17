from BinaryTree import Tree


class SymbolTable:
    def __init__(self):
        self._binaryTree = Tree()

    def add(self, value):
        return self._binaryTree.Insert(value)

    def get(self, value):
        return self._binaryTree.find(value)

    def PrintSymbolTable(self):
        print(self._binaryTree)
