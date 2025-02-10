'''To write a function that checks if the given singly linked list is cyclic or not'''
def cycliccheck(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextNode != None:
        marker1 = marker1.nextNode
        marker2 = marker2.nextNode.nextNode

        if marker2 == marker1:
            return True
    return False

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
c.nextNode = a  # Cycle Here!

print(cycliccheck(a))

x = Node(1)
y = Node(2)
z = Node(3)

x.nextNode = y
y.nextNode = z

print(cycliccheck(x))

