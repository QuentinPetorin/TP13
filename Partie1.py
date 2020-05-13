class Node:
    def __init__(self,val,right,left):
        self.__val = val
        self.__right = right
        self.__left = left

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def getVal(self):
        return self.__val

    def setRight(self,right):
        self.__right = right
        return self.__right

    def setLeft(self,left):
        self.__left = left
        return self.__left

    def aff(self):
        print(self.getVal())
        print(self.getRight())
        print(self.getLeft())




val = 3
right = 2
left = 1
obj = Node(val,right,left)

#print(obj.getRight())
obj.aff()
