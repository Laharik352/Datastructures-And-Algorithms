'''To write a function that takes a head node and an integer value n and then returns the nth to the last node in the linked list'''
#Doubt
def nth_to_lst_node(n, head):
    left_pointer = head
    right_pointer = head
    for i in range(n-1):
        if not right_pointer.nextNode:
            raise LookupError('Error:n is larger than the linked list')
        right_pointer = right_pointer.nextNode

    while right_pointer.nextNode:
        left_pointer = left_pointer.nextNode
        right_pointer = right_pointer.nextNode
    return left_pointer

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

target_node = nth_to_lst_node(2, a)
print(target_node.value)
