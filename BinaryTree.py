from Partie1 import Node

class BinaryTree :
    def __init__(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root




if 'name' == 'main':
    root = 12

    obj1 = BinaryTree(root)
    x = obj1.getRoot().getRight()
    print(x)

