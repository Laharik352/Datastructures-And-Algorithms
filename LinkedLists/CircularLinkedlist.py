'''Implementation of Circular linked lists'''
class doublylinkedlists(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None
a = doublylinkedlists(1)
b = doublylinkedlists(2)
c = doublylinkedlists(3)
a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b
c.nextNode = a
a.prevNode = c

print(a.value)
print(a.nextNode.value)
print(b.prevNode.value)
print(b.value)
print(b.nextNode.value)
print(b.prevNode.value)
print(c.value)
print(c.nextNode.value)
print(c.prevNode.value)
