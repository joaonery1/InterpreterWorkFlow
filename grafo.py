from collections import defaultdict


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
    

import re
import string
lista = []   
with open('interpreterworkflow.wk') as arquivo:
    dados = arquivo.readlines()[57:78]  # array de strings
    # print(dados)
    texto = dados  # varíavel para armazenar o array de string
    for letra in texto:  # for para transformar em string
        # print(letra)
        filtro = re.compile('([0-9]+)')  # pegar só digitos númericos
        
        resp = filtro.findall(letra)  # funcao para trasnformar em números
        #resp = list(map(int, resp))  # função apra transformar em inteiros
        #print(resp)

        print(resp)
        for ares in resp:
            resp = list(map(int, resp))
            lista.append(ares)
arestas = list(map(int,lista))
print(arestas)
print(resp)
print("Tamanho da lista",len(arestas))
n = len(arestas)//2
len_arestas = len(arestas)
splited = []
for i in range(n):
    start = int(i*len_arestas/n)
    end = int((i+1)*len_arestas/n)
    splited.append(arestas[start:end])

print("Saida da lista de nodes:")
print(splited)  
grafo = Grafo(splited,direcionado=True)
print(grafo.get_arestas()[1])
print("====================================")

print("Saida do grafo:")
print(grafo.adj)
print("Saida das arestas:")
print(grafo.get_arestas())
v = grafo.get_arestas()
print("Saida dos vertices:")
print(grafo.get_vertices())
u = grafo.get_vertices()



'fazer implementacao pra saida apontar pra varias entradas  e especificar ql entrada recebe a aresta e qual aresta ai'