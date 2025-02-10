'''Binary search Tree Implementation'''

class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None        # Root is none by default
        self.size = 0           # Default size of the binary search tree is none

    def length(self):
        return self.size

    def __len__(self):          # This allows you to use the built in method of __len__ on the BST
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:                               # When there is no left of right child to search, then, we've found the position where the new node has to be installed
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:       # If the key is less then the current key, then insert the new node in the left
            if currentNode.hasLeftChild():      # if there is a left key already
                self._put(key, val, currentNode.leftChild)
            else:       # if there is not left key, then create a new node and add the new value
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:                           # If the key is greater then the current key, then insert the new node to the right
            if currentNode.hasRightChild():         # If there is a right key already
                self._put(key, val, currentNode.rightChild)
            else:                       # Create a new Tree Node object if there is no key in the right and insert the new node here
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):        # Insert a node with a key and its value
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:

                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):

        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)  #It searches the tree recursively until it gets a non matching leaf node or finds the matching key.
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):     # This makes the current object to look like a dictionary and the values can be easily retrieved
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):       # We are implementing the in operation here using get.
            return True
        else:
            return False

    def delete(self, key):

        if self.size > 1:

            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):

        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():

                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():

                if self.isLeftChild():

                    self.parent.leftChild = self.leftChild
                else:

                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
        else:

            if self.isLeftChild():

                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):

        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()        # if the node getting deleted has a right child, then the successor is going to be the minimum in the right child
        else:
            if self.parent:         # If the node has no right child, and is the left child of its parent, then the parent is the successor

                if self.isLeftChild():

                    succ = self.parent
                else:               #If the node is the right child of its parent, and itself has no right child, then the successor to this node is the successor of its parent excluding this node
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
                            # Using the BST property, the minimum valued key is the left most child in the tree
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):

        if currentNode.isLeaf():  # leaf        # Case-1
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior     # Case:3

            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child        # Case:2
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:

                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:

                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])