'''Write a function to reverse a linked list'''
'''Simple and Easy Method of reversal of a linked list'''
class Node:
    def __init__(self, head):
        self.head = head
        self.next = None
def reverse(head):
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

# print(c.next.head)
reverse(a)

print(d.head)
print(d.next.head)
print(c.next.head)
print(b.next.head)

'''#Doubt
def reverse(head):
    current = head
    previous = None
    nextNode = None

    while current:

        nextNode = current.nextNode
        current.nextNode = previous
        previous = current
        current = nextNode

    return previous

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
# c.nextNode = a

reverse(a)

print(c.value)
print(c.nextNode.value)
print(b.nextNode.value)
'''

