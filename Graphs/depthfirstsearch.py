'''Implementation of depth first search
The implementation below uses the stack data-structure to build-up and return a
set of vertices that are accessible within the subjects connected component.
Using Python’s overloading of the subtraction operator to remove items from a set,
we are able to add only the unvisited adjacent vertices.'''

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):      #start is the starting node or vertex
    visited = set()         #all the visited vertices are in this set
    stack = [start]         # we use stack data structure, we set the stack to the starting node
    while stack:
        vertex = stack.pop()        #if the stack is not empty, we pop it out and add it to the vertex list
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)       #set(['B','C']) - set('B')={'C'}, here we subtracting to get only the unvisited vertices in the stack
    return visited
print(dfs(graph,'A'))       # this is a set, dont worry if the order changes

