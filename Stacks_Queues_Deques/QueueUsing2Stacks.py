'''In this problem, we need to implement a queue usig 2 stacks

The key insight is that a stack reverses order (while a queue doesn't).
A sequence of elements pushed on a stack comes back in reversed order when popped.
Consequently, two stacks chained together will return elements in the same order,
since reversed order reversed again is original order.

We use an in-stack that we fill when an element is enqueued and the dequeue operation takes
elements from an out-stack. If the out-stack is empty we pop all elements from the
in-stack and push them onto the out-stack.'''

class queue2stacks:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enque(self,element):
        self.instack.append(element)        #1,2,3,4,5  # First in is 5

    def deque(self):

        if not self.outstack:       # If the outstack is empty, we pop all the elements from the instack
            while self.instack:
                self.outstack.append(self.instack.pop())  #5,4,3,2,1

        return self.outstack.pop()      #1,2,3,4,5  So, pop is happeing like FIFO  #First out is also 5

#Verification of the implementation
q = queue2stacks()

for i in range(5):
    q.enque(i)          # 0,1,2,3,4

for i in range(5):
    print(q.deque())    # 0,1,2,3,4