class Node:
    def __int__(self, data):
        self.data = data
        self.next = None
    def countNodes(head):
        count = 1
        current = head
        while current.next != None:
            current = current.next
            count += 1
        return count

head = Node(6)
nodeB = Node(5)
nodeC = Node(4)
nodeD = Node(3)
nodeE = Node(2)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
print(head.countNodes())