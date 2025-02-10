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

def buildGraph(wordFile):
    d = {}          
    g = Graph()

    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g