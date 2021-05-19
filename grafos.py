# duncao pra adcioanar o vertice
def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print( v, " vertice existe")  #caso o vertice exista
  else:
    vertices_no = vertices_no + 1
    graph[v] = []

# funcao pra adcionar o vertice e o parametro
def add_edge(v1, v2, e):
  global graph
  # verificar se o v1 eh valido
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # verificar se o v2 eh valido
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e]
    graph[v1].append(temp)

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0])

# driver code
graph = {}
# stores the number of vertices in the graph
vertices_no = 0
add_vertex(1)
add_vertex(3)
add_vertex(5)
add_vertex(7)
add_vertex(11)
add_vertex(15)
add_vertex(17)
add_vertex(19)
add_vertex(21)
add_vertex(13)
add_vertex(9)

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 3, 0)
add_edge(1, 5, 0)
add_edge(1, 7, 3)
add_edge(1, 11, 0)
add_edge(1, 13, 0)
add_edge(1, 15, 0)
add_edge(1, 17, 0)
add_edge(1, 19, 0)



add_edge(3, 5, 0)
add_edge(7, 9, 0)
add_edge(11, 13, 0)
add_edge(15, 17, 0)
add_edge(19, 21, 0)

#print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Representação", graph)