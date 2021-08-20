class Vertex:
    __slots__ = 'key', 'incident_edge', 'outgoing_edge'

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f'Vertex({self.key})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.key)


class Edge:
    __slots__ = 'head_vertex', 'end_vertex', 'directed'

    def __init__(self, head_vertex, end_vertex, directed=True):
        self.head_vertex = head_vertex
        self.end_vertex = end_vertex
        self.directed = directed

    def __str__(self):
        string = f'Edge(head={self.head_vertex}, ' \
                 f'end={self.end_vertex}, ' \
                 f'directed={self.directed})'
        return string

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        if self.directed:
            edge_hash = hash((self.head_vertex, self.end_vertex, self.directed))
        else:
            edge_hash = hash((hash((self.head_vertex, self.end_vertex, self.directed)) + 
                              hash((self.end_vertex, self.head_vertex, self.directed))))
        return edge_hash

    def opposite(self, vertex):
        if vertex != self.head_vertex and vertex != self.end_vertex:
            raise ValueError(f'Vertex {vertex} does not belong to this edge.')
        return self.head_vertex if vertex == self.end_vertex else self.end_vertex

    def endpoints(self):
        return self.head_vertex, self.end_vertex

    def is_directed(self):
        return self.directed


class Graph:
    """

    self.vertices = {key: Vertex}
    self.edges = {hash(Vertex1, Vertex2, directed): Edge}

    """

    __slots__ = 'vertices', 'edges'

    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def __str__(self):
        return f'Graph(vertices={self.vertices}, edges={self.edges})'
    
    def __repr__(self):
        return self.__str__()

    def add_vertex(self, key):
        if key in self.vertices:
            raise KeyError(f'Vertex({key}) is already in the graph.')
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def add_edge(self, head_vertex, end_vertex, directed=True):
        for vertex in [head_vertex, end_vertex]:
            if vertex.key not in self.vertices:
                raise KeyError(f'{vertex} is not in the graph')
        edge = Edge(head_vertex, end_vertex, directed)
        self.edges[hash(edge)] = edge

    def vertex(self, key):
        if key not in self.vertices:
            raise KeyError(f'Vertex({key}) is not in the graph.')
        return self.vertices[key]

    def edge(self, vertex1, vertex2, directed):
        edge_hash = self.edge_hash(vertex1=vertex1, vertex2=vertex2, directed=directed)
        if edge_hash not in self.edges:
            raise KeyError(f'{Edge(vertex1, vertex2, directed)} does not in the graph')
        return self.edges[edge_hash]

    def edge_hash(self, edge=None, vertex1=None, vertex2=None, directed=None):
        if edge:
            return hash(edge)
        if directed:
            edge_hash = hash((vertex1, vertex2, directed))
        else:
            edge_hash = hash((hash((vertex1, vertex2, directed)) + 
                              hash((vertex2, vertex1, directed))))
        return edge_hash


if __name__ == '__main__':
    from pprint import pprint

    g = Graph()
    g.add_vertex(1)
    g.add_vertex(3)
    g.add_vertex(-12)
    # print(g)
    g.add_edge(g.vertex(1), g.vertex(3))
    g.add_edge(g.vertex(3), g.vertex(1))
    g.add_edge(g.vertex(1), g.vertex(3), False)
    pprint(g)

    pprint(g.edge(g.vertex(1), g.vertex(-12), False))

