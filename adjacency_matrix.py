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
    
    def add(self, weight, name=None):
        '''Add a weight to the edge.'''
        if name is None:
            name = weight
        self.weights[name] = weight

    def remove(self, name):
        '''Remove a weight from the edge.'''
        self.weights.pop(name)
    
    def clear(self):
        '''Remove all weights from the edge.'''
        self.weights = {}

# Adjacency Matrix representation in Python
class Graph(object):
  '''A class to represent a directed graph.'''
  # Initialize the matrix
  def __init__(self, size):
    self.adjMatrix = []
    for i in range(size):
      self.adjMatrix.append([Edge() for i in range(size)])
    self.size = size

  # Add edges
  def add_edge(self, v1, v2, weight=1):
    '''
    Add an edge to the graph.
    Args:
        v1 (int): The first vertex.
        v2 (int): The second vertex.
        weight (int): The weight of the edge.'''
    
    if v1 == v2:
      print("Same vertex %d and %d" % (v1, v2))
    self.adjMatrix[v1][v2].add(weight)

  # Remove edges
  def remove_edge(self, v1, v2):
    '''
    Remove an edge from the graph.'''

    self.adjMatrix[v1][v2].clear()

class MultiGraph(Graph):
    '''
    A class to represent a directed graph with multiple edges
    between the same nodes.'''

    def __init__(self, size):
        self.super(size)

    def add_edge(self, v1, v2, weight, name=None):
        '''
        Add an edge to the graph.
        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
            weight (int): The weight of the edge.
            name (str): The name of the edge.'''
        
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        elif name is None:
            self.adjMatrix[v1][v2].add(weight)
        else:
            self.adjMatrix[v1][v2].add(weight, name)
    
    def remove_edge_weight(self, v1, v2, weight, name=None):
        '''
        Remove an edge from the graph.
        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
            weight (int): The weight of the edge.
            name (str): The name of the edge.'''
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        elif name is None:
            self.adjMatrix[v1][v2].remove(weight)
        else:
            self.adjMatrix[v1][v2].remove(name)