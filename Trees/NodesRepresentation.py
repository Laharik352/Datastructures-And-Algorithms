'''Implementation of Nodes and References of a Binary Tree'''
class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj  # set the key equal to that root node
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode) #Here we are creating a new instance of the Binary tree from this node
        else:           # Here we are pushing down the already existing node to a new level
            t = BinaryTree(newNode)     #We create a new binary tree with the new node as the root node
            t.leftChild = self.leftChild    # We move the already existing node to the left of the new binary tree
            self.leftChild = t      # Now, we put this new binary tree to the main left position

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild  #right child of the current object reference

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
#
# def preorder(tree):
#     if tree:
#         print(tree.getRootval())
#         preorder(tree.getLeftChild())
#         preorder(tree.getRightChild())
#
# def inorder(tree):
#     if tree:
#         inorder(tree.getLeftChild())
#         print(tree.getRootval())
#         inorder(tree.getRightChild())
#
# def postorder(tree):
#     if tree:
#         postorder(tree.getLeftChild())
#         postorder(tree.getRightChild())
#         print(tree.getRootval())


r = BinaryTree('a')
print(r)
print(r.getRootVal())
print(r.getLeftChild())
print(r.getRightChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())    #We are referring to the sub tree here
r.insertLeft('c')
print(r.getLeftChild().getRootVal())        # c
print(r.getLeftChild().getLeftChild())
print(r.getLeftChild().getLeftChild().getRootVal())     #b- b has been pushed down to one level
r.getLeftChild().insertLeft('d')
print(r.getLeftChild().getLeftChild().getRootVal())

# print(preorder(r))

