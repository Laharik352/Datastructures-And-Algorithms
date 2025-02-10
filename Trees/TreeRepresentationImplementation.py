def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

s = BinaryTree(3)
print("r: ", s)
insertLeft(s, 4)
print("rinsertLeft: ", s)
insertLeft(s, 5)
print("rinsertLeft: ", s)
insertRight(s,6)
print('insertRight:', s)
insertRight(s,7)
print('insertRight:', s)

l = getLeftChild(s)
print(l)
setRootVal(l,9)
print(s)
setRootVal(s,9)
print(s)