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
    __slots__ = 'head_vertex', 'end_vertex'

    def __init__(self, head_vertex, end_vertex):
        self.head_vertex = head_vertex
        self.end_vertex = end_vertex

    def __str__(self):
        string = f'Edge(head={self.head_vertex}, end={self.end_vertex})'
        return string

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.head_vertex, self.end_vertex))

    def opposite(self, vertex):
        if vertex != self.head_vertex and vertex != self.end_vertex:
            raise ValueError(f'Vertex {vertex} does not belong to this edge.')
        return self.head_vertex if vertex == self.end_vertex else self.end_vertex

    def endpoints(self):
        return self.head_vertex, self.end_vertex


class Graph:
    """

    Graph.vertices is a structure of {Vertex1:{True: set(), False: set()}, Vertex2:...}.
    Inside a vertex is another dictionary which contains two sets, one for containing
    outgoing edges (key 'True'), the other for incident edges (key 'False').

    If one edge is an undirected edge, it will be saved in the 'True' set inside the 
    head_vertex of self.vertices.

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
            raise KeyError(f'{key} has already in graph.')
        self.vertices[key] = {True: set(), False: set()}

    def add_edge(self, head_vertex, end_vertex, outgoing_edge=True):
        for vertex in [head_vertex, end_vertex]:
            if vertex not in self.vertices:
                raise KeyError(f'{vertex} is not in the graph')
        edge = Edge(head_vertex, end_vertex)
        self.edge[edge] = edge
        self.vertices[head_vertex][True].add(edge)
        self.vertices[end_vertex][outgoing_edge].add(edge)


if __name__ == '__main__':
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(1)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v2)
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(1)
    print(g)

