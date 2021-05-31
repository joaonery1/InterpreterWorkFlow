
import re
import os
import string

# -*- coding: utf-8 -* 
from collections import defaultdict

#funcao para fazer sublistas dado um N
def chunks(lista,n):
    for i in range(0,len(lista),n):
        yield lista[i:i +n]
   

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
def node_connection_parameters(lstu,lstv,listin,listout,listassc):
    if os.path.isfile("interpreterworkflow.wk"):
        file1 = open("interpreterworkflow.wk","r")
        for line in file1:
            if 'nodeconnection' in line.lower():
                conexao = line.split(':')
                lstu.append(conexao[1])
                lstu.append(conexao[3])
                lstv.append(conexao[3])
                listin.append(conexao[4])
                listout.append(conexao[2])
                listassc.append(conexao[1])
                listassc.append(conexao[2])
                listassc.append(conexao[3])
                listassc.append(conexao[4])
                #pensar em outra forma de aramazenar nessa lista os parametros associados
                #dessa forma pode dizer que ele está associado?
                #pensar em criar uma funcao apenas para ler parametros? Ou funcao para ler os dois?
                #verificar um jeito de tirar o '/n' no final de caracter no .split 
                #talvez criar uma função para transformar uma lista de str em int, ao inves de fazer um for na 'raiz'
        file1.close()

#script para leitura do arquivo e aplicao das funcoes

lstarestas= []

lstv = []
listout= []
listin = []
listassc = []
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
#print(lista_arestas)
#print(lista_vertices)

#aplicação da função
lstu1 = []
node_connection_parameters(lstu1,lstv,listin,listout,listassc)




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
l_de_vertices = [1,2,3,4,5,6,7,8,9,10]
l_de_arestas = [[1, 2], [1, 6], [1, 8], [3, 6], [3, 10], [5, 2], [5, 4], [7, 4], [7, 8], [9, 2], [9, 4]]
'''
grafo = cria_grafo(lista_vertices,lista_arestas)

print("Representação\n",grafo)
print("####################################")
caminhos = list(dfs_caminhos(grafo,1,9))
print("Caminhos percorridos\n",caminhos)
print("####################################")

#separa em sublistas
lista_assc = list(chunks(listassc,4))
print(lista_assc)

'''
implementar para um grafo junto com os parametros
'''