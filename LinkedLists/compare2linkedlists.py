# Python program to compare two linked lists, return 1 if they are same, return 0 if they are not
class Node:
    def __init__(self, value):
        self.head = value
        self.next = None

def compare(list1, list2):
    while (list1 and list2 and list1.head==list2.head):
        list1 = list1.next
        list2 = list2.next
    if (list1 and list2):
        return 1 if (list1.head==list2.head) else 0
        # return 0
    if (list1 and not list2):
        return 0
    if (list2 and not list1):
        return 0
    return 1

a = Node("e")
a.next = Node("s")
a.next.next = Node("h")
a.next.next.next = Node("w")
a.next.next.next.next = Node("a")
a.next.next.next.next.next = Node("r")

b = Node("e")
b.next = Node("s")
b.next.next = Node("h")
b.next.next.next = Node("w")
b.next.next.next.next = Node("a")
b.next.next.next.next.next = Node("k")

print(compare(a,b))