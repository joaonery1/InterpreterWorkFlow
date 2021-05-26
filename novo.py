class Grafo(object):

    def __init__(self, vertices,arestas,lista_i,lista_o):
        self.vertices = vertices
        self.adiciona_aresta(self,arestas,lista_i,lista_o)
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, lista_i,lista_o):
        # estamos pensando em grafo direcionado com peso nas arestas
        # self.grafo[u-1].append([v,lista_i,lista_o])


        self.grafo[v-1].append([u,lista_i,lista_o])

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

# g = Grafo(4)
arestas = (1,2)
lista_i = ['o']
lista_o = ['i']
g =Grafo(1,arestas,lista_i,lista_o)
# g.adiciona_aresta(1, 2, 5,4)
# g.adiciona_aresta(1, 2, 5,4)
# g.adiciona_aresta(1, 3, 7,5)
# g.adiciona_aresta(1, 4, 6,6)
# g.adiciona_aresta(2, 3, 9,3)
g = Grafo()
g.mostra_lista()