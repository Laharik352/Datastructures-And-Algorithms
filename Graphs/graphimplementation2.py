'''implement a simple graph by focusing on the Node class'''

from enum import Enum
class State(Enum):
    unvisited = 1 #White
    visited = 2 #Black
    visiting = 3 #Gray



from collections import OrderedDict

class Node:

    def __init__(self, num):
        self.num = num          #This stores the ID of the node
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight #Using orderedDict since it will be useful for BFS and DFS

    def __str__(self):
        return str(self.num)


class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight


g = Graph()
g.add_edge(0, 1, 5)
print(g.nodes)
g.add_edge(1,2,3)
print(g.nodes)