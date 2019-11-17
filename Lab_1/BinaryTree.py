class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def Insert(self, item):
        if self.find(item) is False:
            newNode = Node(item)
            current = self.root
            parent = self.root

            if self.root is None:
                self.root = newNode
            else:
                while current is not None:
                    parent = current
                    if item < current.data:
                        current = current.lChild
                    else:
                        current = current.rChild

                if item < parent.data:
                    parent.lChild = newNode
                else:
                    parent.rChild = newNode

    def makeList(self, aNode):
        if aNode is None:
            return []
        return self.makeList(aNode.lChild) + [aNode.data] + self.makeList(aNode.rChild)

    def __str__(self):
        lista = self.makeList(self.root)
        s = ''
        for i in range(len(lista)):
            s += str(lista[i]) + ' ' + str(i) + '\n'
        return s

    def find(self, value):
        try:
            BTlist = self.makeList(self.root)
            return BTlist.index(value)
        except ValueError:
            return False

# root = Tree()
# root.Insert('c')
# root.Insert('x')
# root.Insert('a')
# root.Insert('b')
# print(root.makeList(root.root))
# print(root.find('p'))
