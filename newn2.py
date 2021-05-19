class Graph2(object):
    
    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
        it, i.e. the number of adjacent vertices. Loops are counted 
        double, i.e. every occurence of vertex in the list 
        of adjacent vertices. """ 
        degree =  len(self._graph_dict[vertex]) 
        if vertex in self._graph_dict[vertex]:
            degree += 1
        return degree

    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self._graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated
        
    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self._graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max
    
    def degree_sequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self._graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

g = { "1" : {"3,5,7,11,15,19"},
      "3" : {"5"},
      "7" : {"9"},
      "11" : {"13"},
      "15" : {"17"},
      "19" : {"21"}
    }
graph = Graph2(g)
path = graph.find_isolated_vertices()
print(path)
