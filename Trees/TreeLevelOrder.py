'''Given a binary tree of integers, print it in level order. The output will contain space between the
numbers in the same level, and new line between different levels.'''

import collections
class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount = 1
    nextCount = 0

    while len(nodes) != 0:      #As long as the nodes are present
        currentNode = nodes.popleft()
        currentCount = currentCount - 1
        print(currentNode.val)

        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1

        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1

        if currentCount == 0:
            # print("\n")     # After all the elements in that level have been completed, go to the next level
            # print(currentCount)
            # print(nextCount)
            # print("OOOOOO")
            currentCount, nextCount = nextCount, currentCount
            # print(currentCount)
            # print(nextCount)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
levelOrderPrint(root)


