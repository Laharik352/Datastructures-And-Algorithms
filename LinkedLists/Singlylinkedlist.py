'''Implementation of Singly linked lists'''
class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None #The default value of the node will be None, so the next node of c will be None
a = Node(1)
b = Node(2)
c = Node(3)
a.nextNode = b
b.nextNode = c

print(a.value)
print(a.nextNode.value)
print(b.value)
print(b.nextNode.value)
print(c.value)
