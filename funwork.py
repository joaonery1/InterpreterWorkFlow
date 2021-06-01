
import re
import os
import string

# -*- coding: utf-8 -* 
from collections import defaultdict

class objGlyph(object):
    def __init__(self, vglyph_id,):       
        self.glyph_id = vglyph_id    
    
    def __repr__(self):
        return "{}".format(self.glyph_id)



class objConnection(object):

    def __init__(self,u_id,u_output,v_id,v_input):

        self.u_id= u_id
        self.u_output = u_output
        self.v_id = v_id
        self.v_input = v_input
    
    def __repr__(self):
        return "{},{}".format(self.u_output,self.v_input)

    def chunks(lista,n):
        for i in range(0,len(lista),n):
            yield lista[i:i +n]
        return list(lista)

lstConnection = []
vConnection = objConnection
vGlyph = objGlyph

#funcao para fazer sublistas dado um N
def chunks(lista,n):
    for i in range(0,len(lista),n):
        yield lista[i:i +n]
   
#funcao teste para str - > int
def int_str(lst):
    lst = []
    lista_n = []
    for valores in lst:
        lista_n.append(int(valores))
    return lista_n

def vertex_graph(lstv):
    if os.path.isfile("arquivo2.wk"):
        file1 = open("arquivo2.wk","r")
        for line in file1:
            if 'glyph:' in line.lower():
                vertex = line.split(':')
                lstv.append(vertex[3])
        file1.close()

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


#ideia de leitura com parametros
def connection_parameters(lstGlyph):
    if os.path.isfile("interpreterworkflow.wk"):
        file1 = open("interpreterworkflow.wk","r")
        
        for line in file1:
            if 'glyph:' in line.lower():
                conexao = line.split(':')
                vGlyph = objGlyph(conexao[3])
                lsti.append(vGlyph)

            if 'nodeconnection' in line.lower():
                conexao = line.split(':')
                vConnection = objConnection(conexao[1],conexao[2],conexao[3],conexao[4])
                lstConnection.append(vConnection)
        file1.close()

lstGlyph = []
lstConnection = []
lstedge = []
lstparam = []
lstedges = []
lsti = []
lstvertex = []
connection_parameters(lstGlyph)
for vConnection in lstConnection:
    lstedge.append(vConnection.u_id)
    lstedge.append(vConnection.v_id)
    lstparam.append(vConnection.u_output)
    lstparam.append(vConnection.v_input)
    #print(vConnection.u_id,vConnection.v_id)

for vGlyph in lstGlyph:
    lsti.append(vGlyph.vglyph_id)


for val in lstedge:
    lstedges.append(int(val))

print(lsti)
lstedges = list(chunks(lstedges,2))
lstcomplete= [*sum(zip(lstedges,lstparam),())]    #juntei depois de alimentar a lista
lstcomplete = list(chunks(lstcomplete,4))    

print(lsti)   #lista de vertices 
print(lstedges) #lista de arestas
print(lstcomplete) #lista arestas c/ parametros


############################################################

#script para leitura do arquivo e aplicao das funcoes
lstarestas= []
lstv = []
listout= []
listin = []
listassc = []

vertex_graph(lstv)
node_connection(lstarestas)
#tratamento, str -> int
lista_arestas = []
lista_vertices = []
for val in lstarestas:
    lista_arestas.append(int(val))
for val in lstv:
    lista_vertices.append(int(val))
lista_arestas = list(chunks(lista_arestas,2)) #nova lista tratada
lstarestas = list(chunks(lstarestas,2))       #nova lsita tratada

#função para criar grafo
def cria_grafo(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])
        grafo[aresta[1]].append(aresta[0])
    return grafo    

#função que percorre o grafo inicio->fim
def dfs_caminhos(grafo, inicio, fim):
    pilha = [(inicio, [inicio])]
    while pilha:
        vertice, caminho = pilha.pop()
        for proximo in set(grafo[vertice]) - set(caminho):
            if proximo == fim:
                yield caminho + [proximo]
            else:
                pilha.append((proximo, caminho + [proximo]))

'''
lista genérica

'''
l_de_vertices = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]
l_de_arestas = [[1, 2], [1, 6], [1, 8], [3, 6], [3, 10], [5, 2], [5, 4], [7, 4], [7, 8], [9, 2], [9, 4]]

grafo = cria_grafo(l_de_vertices,l_de_arestas)

print("Representação\n",grafo)
print("####################################")
#caminhos = list(dfs_caminhos(grafo,1,9))
#print("Caminhos percorridos\n",caminhos)
print("####################################")

#separa em sublistas
#lista_assc = list(chunks(listassc,4))
lista_asso = []





'''
verificar erro ao ao criar o grafo com a lista de objtos
'''