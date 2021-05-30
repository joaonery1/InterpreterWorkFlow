
import re
import os
import string

from collections import defaultdict

#funcao para fazer sublistas dado um N
def chunks(lista,n):
    for i in range(0,len(lista),n):
        yield lista[i:i +n]
   
    
def node_connection(lstu):
    if os.path.isfile("arquivo2.wk"):
        file1 = open("arquivo2.wk","r")
        for line in file1:
            if 'nodeconnection' in line.lower():
                conexao = line.split(':')
                conexao.remove('\n')
                #conexao = line.rstrip('\n')
                lstu.append(conexao[1])
                lstu.append(conexao[2])
                #lstinp.append(conexao[5])
                #lstout.append(conexao[3])
        file1.close()


#script para leitura do arquivo e aplicao das funcoes

lstarestas= []
lstout = []
lstv = []
lstinp = []
'''
with open('interpreterworkflow.wk') as file:
    for line in file:
        if 'nodeconnection' in line.lower():
            # entradas = fun_node(line) #recebe as duas listas de parametros
            # arestas = fun_duplas(line)   #recebe as arestas 
            conexao = line.split(':')
            lstu.append(conexao[2],)
            lstu.append(conexao[4])
            lstout.append(conexao[3])
            lstout.append(conexao[5])

            
        elif 'glyph' in line.lower():
            fun_gliph(line)       
            vertices = fun_vertex(line) #recebe a lista de vertices
            #funcao para tratar os glyphos e suas variaveis
'''
#print(lstu,lstout)

node_connection(lstarestas)
lista_arestas = []

for val in lstarestas:
    lista_arestas.append(int(val))
lista_arestas = list(chunks(lista_arestas,2))
lstarestas = list(chunks(lstarestas,2))
#print(lista_arestas)
#print(lstarestas)
lista_de_vercites = [1,3,5,7,9]
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
    

def cria_grafo(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[1]].append(aresta[0])
    return grafo
def dfs_caminhos(grafo, inicio, fim):
    pilha = [(inicio, [inicio])]
    while pilha:
        vertice, caminho = pilha.pop()
        for proximo in set(grafo[vertice]) - set(caminho):
            if proximo == fim:
                yield caminho + [proximo]
            else:
                pilha.append((proximo, caminho + [proximo]))
def gerar_caminhos(grafo, caminho, final):
    """Enumera todos os caminhos no grafo `grafo` iniciados por `caminho` e que terminam no vértice `final`."""

    # Se o caminho de fato atingiu o vértice final, não há o que fazer.
    if caminho[-1] == final:
        yield caminho
        return

    # Procuramos todos os vértices para os quais podemos avançar…
    for vizinho in G[caminho[-1]]:
        # …mas não podemos visitar um vértice que já está no caminho.
        if vizinho in caminho:
            continue
        # Se você estiver usando python3, você pode substituir o for
        # pela linha "yield from gerar_caminhos(grafo, caminho + [vizinho], final)"
        for caminho_maior in gerar_caminhos(grafo, caminho + [vizinho], final):
            yield caminho_maior

grafo = Grafo(lista_arestas,direcionado=True)
dic1 = grafo.adj
for caminho in gerar_caminhos(dic1,1,9):
    print (caminho)
print(dic1)
caminhos = list(dfs_caminhos(dic1,1,9 ))
print(caminhos)
