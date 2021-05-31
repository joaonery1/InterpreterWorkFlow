# funcao pra adcioanar o vertice

def __init__(self):
  self.add_vertex()

def add_vertex(v):
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

#funcao para armazenar os parametros
def fun_node(var):
    var = var.split(':')
    var = var[2::]
    #print(var)
    lista_entrada = []
    lista_saida = []
    lista_entrada.append(var[3])
    lista_saida.append(var[1])
    return lista_entrada,lista_saida

#funcao para armazenar as arestas
def fun_duplas(parametros):
    lista = []
    filtro = re.compile('([0-9]+)')
    resp = filtro.findall(parametros)
    for duplas in resp:
        resp = list(map(int,resp))
        lista.append(duplas)   
    arestas = list(map(int,lista))
    return arestas

    
#funcao a ser trabalhada para armazenar as informacoes dos glifos
def fun_gliph (var):
    var = var.split(':')
    #talvez usar o regex
    novos_dados = ''
    novos_dados+= '{};{};{};{};{};{};{};{};{};{}\n'.format(var[:4],var[4:7],var[7:11],var[11:13],var[13:15],var[15:17],
    var[17:18],var[18:25],var[25:26],var[26:32],var[32:33])
    content = '{}\n{}'.format(';'.join(var),novos_dados)


    #funcao para pegar os vertices dos glifos
def fun_vertex(vertex): 
    vertex = vertex.split(':')
    vertex = vertex[3]
    valores = []
    lista_vertices = []
    valores.append(vertex)
    for i in valores: #for para passar uma lista de inteiros
        lista_vertices.append(int(i))
    return lista_vertices


class Grafo(object):
    """ Implementação básica de um grafo. """
    
    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas) 
        


    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())


    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [([k, v]) for k in self.adj.keys() for v in self.adj[k]]


    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v in arestas:
            self.adiciona_arco(u, v)


    def adiciona_arco(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)


    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]
    