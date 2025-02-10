'''Implementation of Queues'''
class Queues:
    def __init__(self):
        self.items = []
    def enque(self, item):
        self.items.insert(0,item) #0 for inserting the element at the rear end of the queue
    def deque(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items) == []
    def size(self):
        return len(self.items)
q = Queues()
print(q.isEmpty())
print(q.enque(1))
print(q.enque("two"))
print(q.size())
print(q.enque(True))
print(q.deque())
print(q.deque())