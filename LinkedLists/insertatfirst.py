# Program to insert a node at the beginning of a linked list

class Node:
    def __init__(self, value):
        self.head = value
        self.next = None

    # This function is in LinkedList class
    # Function to insert a new node at the beginning
def push(head, new_data):
    # 1 & 2: Allocate the Node &
    #        Put in the data
    new_node = Node(new_data)

    # 3. Make next of new Node as head
    new_node.next = head

    # 4. Move the head to point to new Node
    head = new_node
    print("head", head.head)
    return head

b = Node("e")
b.next = Node("s")
b.next.next = Node("h")
b.next.next.next = Node("w")
b.next.next.next.next = Node("a")
b.next.next.next.next.next = Node("k")

push("e", "N")
print(b.head)
print(b.next.head)
print(b.next.next.head)
print(b.next.next.next.head)
print(b.next.next.next.next.head)
print(b.next.next.next.next.next.head)