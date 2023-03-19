class Edge:
    '''
    A class to represent an edge in a graph.
    Attributes:
        weights (dict): A dictionary of weights for the edge.'''

    def __init__(self, weights=None):
        if weights is None:
            self.weights = {}
        else:
            self.weights = dict(zip(weights, weights))

    def __str__(self) -> str:
        return str(self.weights)

    def __len__(self):
        return len(self.weights)
    
    def __repr__(self) -> str:
        return str(self.weights)

    def add(self, weight: int, info:object=None):
        '''Add a weight to the edge.'''
        if info is None:
            info = weight
        self.weights[info] = weight
    
    def get(self, info:object=None):
        '''Get a weight from the edge or the first one if name is None.'''
        if info is None:
            return self.weights[list(self.weights.keys())[0]]
        return self.weights[info]

    def remove(self, info):
        '''Remove a weight from the edge.'''
        self.weights.pop(info)

    def clear(self):
        '''Remove all weights from the edge.'''
        self.weights = {}
    
    def get_infos(self):
        '''Returns a list with the infos of the edge.'''
        return list(self.weights.keys())

# Adjacency Matrix representation in Python


class Graph(object):
    '''
    A class to represent a directed graph.
    Attributes:
        adjList (dic): A dic of lists to represent an adjacency list.
        size (int): The size of the matrix.''
        nodeInfo (list): A list with information for the nodes in the graph, if any.
    Each node is represented by a row and column in the matrix.
    The row represents the edges leaving the node, and the column represents the edges entering the node.'''
    # Initialize the matrix

    def __init__(self, size: int, nodeInfo=None):
        '''
        Initialize the graph.
        Args:
            size (int): The size of the matrix.
            nodeInfo (list): A list of info for the nodes in the graph, if any, having as value the position in the array.'''
        self.adjList = {}
        for i in range(size):
            self.adjList[nodeInfo[i]]={}

        self.size = size

    def __iter__(self):
        self.__iter = iter(self.adjList)
        return self

    def __next__(self):
        return next(self.__iter)
    
    def __getitem__(self, key):
        return self.adjList[key]

    def get_vertices(self):
        '''
        Get the vertices of the graph.
        Returns:
            list: Dict keys object with the vertices.'''
        return self.adjList.keys()
    
    def get_neighbors(self, v):
        '''
        Get the neighbors of a vertex.
        Args:
            v (int): The vertex.
        Returns:
            list: A list with the neighbors.'''
        return self.adjList[v]

    # Add edges
    def add_edge(self, v1, v2, weight=1, name=None):
        '''
        Add an edge to the graph.
        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
            weight (int): The weight of the edge.'''

        #if v1 == v2:
        #    print("Same vertex %s and %s" % (v1, v2))
        if v2 not in self.adjList[v1]:
            self.adjList[v1][v2] = Edge()
        self.adjList[v1][v2].add(weight, name)
    

    # Remove edges
    def remove_edge(self, v1, v2):
        '''
        Remove an edge from the graph.'''

        self.adjList[v1][v2].clear()

    # Get edge weight
    def get_edge_weight(self, v1, v2):
        '''
        Get the weight of an edge.
        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
        Returns:
            int: The weight of the edge.'''
        return self.adjList[v1][v2].get()

class MultiGraph(Graph):
    '''
    A class to represent a directed graph with multiple edges
    between the same nodes.'''

    def __init__(self, size, nodeInfo=None):
        super().__init__(size, nodeInfo)

    def remove_edge_weight(self, v1, v2, weight, name=None):
        '''
        Remove an edge from the graph.
        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
            weight (int): The weight of the edge.
            name (str): The name of the edge.'''
        #if v1 == v2:
        #    print("Same vertex %d and %d" % (v1, v2))
        if name is None:
            self.adjList[v1][v2].remove(weight)
        else:
            self.adjList[v1][v2].remove(name)
    
    def get_edge(self, v1, v2, name=None):
        '''
        Get the weight of an edge.
        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
            name (str): The name of the edge.
        Returns:
            int: The weight of the edge.'''
        if name is None:
            return self.adjList[v1][v2].get()
        else:
            return self.adjList[v1][v2].get(name)
