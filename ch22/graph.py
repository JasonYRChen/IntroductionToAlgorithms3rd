"""
This is not the final code for a graph. An ideal graph should be O(1) operation
among the following action:
1. Add a vertex
2. Add an edge
3. Delete a vertex (the corresponding edges should also be deleted)
4. Delete an adge
5. Lookup for a vertex
6. Lookup for an edge

This version has not achieved the 3rd operation.
"""


class Vertex:
    __slots__ = 'key'

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

    def edge_hash(self, head_vertex, end_vertex, directed):
        if directed:
            edge_hash = hash((head_vertex, end_vertex, directed))
        else:
            edge_hash = hash((hash((head_vertex, end_vertex, directed)) + 
                              hash((end_vertex, head_vertex, directed))))
        return edge_hash

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

    def delete_vertex(self, key):
        pass

    def delete_edge(self, head_vertex, end_vertex, directed):
        edge_hash = self.edge_hash(head_vertex, end_vertex, directed)
        if edge_hash not in self.edges:
            raise KeyError(f'{Edge(head_vertex, end_vertex, directed)} does not exist.')
        del self.edges[edge_hash]

    def vertex(self, key):
        if key not in self.vertices:
            raise KeyError(f'Vertex({key}) is not in the graph.')
        return self.vertices[key]

    def edge(self, head_vertex, end_vertex, directed):
        edge_hash = self.edge_hash(head_vertex, end_vertex, directed)
        if edge_hash not in self.edges:
            raise KeyError(f'{Edge(head_vertex, end_vertex, directed)} does not in the graph')
        return self.edges[edge_hash]

    def vertex_length(self):
        return len(self.vertices)

    def edge_length(self):
        return len(self.edges)

    def edge_between_vertices(self, head_vertex, end_vertex):
        edges = set()
        edge_hashes = [self.edge_hash(head_vertex, end_vertex, True),
                       self.edge_hash(end_vertex, head_vertex, True),
                       self.edge_hash(head_vertex, end_vertex, False)]
        for edge_hash in edge_hashes:
            if edge_hash in self.edges:
                edges.add(self.edges[edge_hash])
        return edges


if __name__ == '__main__':
    from pprint import pprint

    g = Graph()
    g.add_vertex(1)
    g.add_vertex(3)
    g.add_vertex(-12)
    # print(g)
    g.add_edge(g.vertex(1), g.vertex(3))
    g.add_edge(g.vertex(3), g.vertex(1))
    pprint(g)
    pprint(g.edge_between_vertices(g.vertex(1), g.vertex(3)))
    pprint(g.edge_between_vertices(g.vertex(3), g.vertex(1)))
    g.delete_edge(g.vertex(1), g.vertex(3), True)
    g.delete_edge(g.vertex(3), g.vertex(1), True)
    pprint(g)
