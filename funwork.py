
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
    if os.path.isfile("arquivos.wk/"):
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
    if os.path.isfile("arquivos.wk/data.wksp"):
        file1 = open("arquivos.wk/data.wksp","r")
        
        for line in file1:
            if 'glyph:' in line.lower():
                conexao = line.split(':')
                vGlyph = objGlyph(conexao[5])
                lsti.append(vGlyph)

            if 'nodeconnection' in line.lower():
                conexao = line.split(':')
                vConnection = objConnection(conexao[2],conexao[3],conexao[4],conexao[5])
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
    lstparam.append(vConnection.u_output)
    lstedge.append(vConnection.v_id)
    lstparam.append(vConnection.v_input)
    #print(vConnection.u_id,vConnection.v_id)

for vGlyph in lstGlyph:
    lsti.append(vGlyph.vglyph_id)


for val in lstedge:
    lstedges.append(int(val))

for val1 in lsti:
    lstvertex.append(str(val))

    



lstcomplete= [*sum(zip(lstedges,lstparam),())]    #juntei depois de alimentar a lista
lstedges = list(chunks(lstedges,2))
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

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

l_de_vertices = lsti
l_de_arestas = lstedges

lv = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 1, 3, 5, 7, 13, 37, 39, 41, 43, 45, 47, 49, 51, 53, 90, 93]
la = [[1, 13], [3, 5], [3, 7], [3, 1], [3, 13], [5, 7], [5, 1], [7, 1], [11, 5], [13, 9], [1, 3], [3, 5], [3, 39], [5, 7], [5, 53], [7, 33], [7, 31], [9, 37], [11, 9], [13, 11], [15, 9], [15, 13], [17, 15], [19, 9], [19, 17], [21, 19], [23, 25], [25, 9], [25, 21], [27, 9], [27, 
31], [29, 27], [31, 23], [33, 29], [35, 49], [39, 51], [39, 21], [41, 13], [43, 17], [47, 35], [49, 1], [51, 45], [53, 21], [53, 17], [53, 13], [90, 47], [93, 39], [93, 43], [93, 41]]

lv = remove_repetidos(lv)
la = remove_repetidos(la)

print(lv)
grafo = cria_grafo(lv,la)

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