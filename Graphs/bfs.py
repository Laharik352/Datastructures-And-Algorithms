from queue import Queue


def bfs(g, start):      # it takes in a graph and the start point
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()       # Start exploring the vertices at the front of the queue by iterating/dequeueing. Each time the element color is checked
        for nbr in currentVert.getConnections():
            if (nbr.getColor()=='white'):   #if the vertex is unexplored, 4 things happen. All the vertices are initialized to white when they are constructed
                nbr.setColor('gray')        # The new unexplored vertex is colored gray, when the vertex is first initially discovered
                nbr.setDistance(currentVert.getDistance()+1)        #the distance to nbr is set to the distance to the currentVert+1
                nbr.Pred(currentVert)       #the predessesor of nbr is set to the currentVert
                vertQueue.enqueue(nbr)      #adding nbr to the end of the queue which makes it be available for further exploration
        currentVert.setColor('black')       # When the vertex is completely explored, then its colored black
