'''Stacks implementation'''
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == []
    def pop(self):
        return self.items.pop()
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s = Stack()
print(s.isEmpty())
print(s.push(1))
print(s.push("two"))
print(s.peek())
print(s.push(True))
print(s.size())
print(s.pop())
print(s.peek())
print(s.isEmpty())