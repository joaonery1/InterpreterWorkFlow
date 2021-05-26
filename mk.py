# funcao pra adcioanar o vertice

def __init__(self):
  self.add_vertex()

def add_vertex(*v):
  global graph
  global vertices_no
  if v in graph:
    print( v, " vertice existe")  #caso o vertice exista
  else:
    vertices_no = vertices_no + 1
    graph[v] = []


# funcao pra adcionar o vertice e o parametro
def add_edge(v1, v2, lista_entrada, lista_saida):
  global graph

  # verificar se o v1 eh valido
  if v1 not in graph:
    print("Vertice ", v1, " não existe.")
  # verificar se o v2 eh valido
  elif v2 not in graph:
    print("Vertice", v2, " nao existe")
  else:
    temp = [v2]
    inputs = [lista_entrada]
    outputs = [lista_saida]
    graph[v1].append(temp)
    graph[v1].append(inputs)
    graph[v1].append(outputs)

def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0])

'''
Dados:1:o:3:i
mediadp:3:o:5:i
media:5:o:i:9
mediadp:3:o1:5:i1
desvio_padrao:7:o:i:11
'''


graph = {}
vertices_no = 0
add_vertex(1, 3, 5, 7, 9)
add_vertex(1)
add_vertex(3)
add_vertex(5)
add_vertex(7)
add_vertex(9)
add_vertex(11)

add_edge(1, 3,'o','i')
add_edge(3, 5, 'o','i')
add_edge(3, 7,'o1','i1')
add_edge(5, 9,'o','i')
add_edge(7,11,'o','i')

print ("Representação", graph)
'''
output
{1: [[1, 'i', 3, 'o']], 3: [[3, 'i', 5, 'o'], [3, 'i1', 7, 'o1']], 
5: [[5, 'i', 9, 'o']], 7: [[7, 'i', 11, 'o']], 9: [], 11: []}
'''