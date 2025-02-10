'''Here, we ara going to implement a graph using adjacency list
Using dictionaries, it is easy to implement the adjacency list in Python.
In our implementation of the Graph abstract data type we will create two classes:
Graph, which holds the master list of vertices, and Vertex, which will represent each vertex in the graph.

Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge.
This dictionary is called connectedTo. The constructor simply initializes the id, which will typically be
a string, and the connectedTo dictionary. The addNeighbor method is used add a connection from this
vertex to another. The getConnections method returns all of the vertices in the adjacency list, as represented
by the connectedTo instance variable. The getWeight method returns the weight of the edge
from this vertex to the vertex passed as a parameter.'''

class Vertex: #This class is to represent each and every vertex in the graph

    def __init__(self, key):        #Creating a vertex object
        self.id=key                 # Initializes the ID
        self.connectedTo = {}       # Holds the list of all the connected vertices

    def addNeighbour(self,nbr,weight=0):  #To add a connection from this vertex to another
        self.connectedTo[nbr] = weight    # The nbr will be the key and the weight will be the value for the connectedTo dictionaary

    def getConnections(self):
        return self.connectedTo.keys()  #It will return all the keys in the dictionary

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]    # It returns the value associated to the key-->nbr

    def __str__(self):
        return str(self.id)+ " connected to " + str([x.id for x in self.connectedTo])


class Graph:

    def __init__(self):      #This initializes the graph object with the number of vertices
        self.vertList = {}      # shows the list of vertices, this is a dictionary but calling it as a list since it is in a adjacency list form
        self.numvertices = 0

    def addVertex(self, key):   #To add a vertex to the graph
        self.numvertices = self.numvertices + 1   #incrementing the number by 1
        newVertex = Vertex(key)     # creating a new vertex object
        self.vertList[key] = newVertex      #adding the new vertex to the vertlist of the graph
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:      #When you call self.vertlist, it means that you are searching for n in the keys of the vertlist
            return self.vertList[n]
        else:
            return None

    def addEdge(self,f,t,cost=0):       # Creating an edge between two vertices
        if f not in self.vertList:      #if the vertices are not present, create a new vertex and then create an edge
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbour(self.vertList[t], cost)   # Else, create an edge between the already existing vertices

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self, n):
        return n in self.vertList


g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
g.addEdge(0,1,2)
for vertex in g:
    print(vertex)
    print(vertex.getConnections())





