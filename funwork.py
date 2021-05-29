
import re
import os
import string
from collections import defaultdict

#funcao para fazer sublistas dado um N
def chunks(lista,n):
    for i in range(0,len(lista),n):
        yield lista[i:i +n]

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
    
    
def node_connection(lstu,lstout,lstinp):
    if os.path.isfile("interpreterworkflow.wk"):
        file1 = open("interpreterworkflow.wk","r")
        for line in file1:
            if 'nodeconnection' in line.lower():
                conexao = line.split(':')
                lstu.append(conexao[2])
                lstu.append(conexao[4])
                lstinp.append(conexao[5])
                lstout.append(conexao[3])

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

node_connection(lstarestas,lstout,lstinp)
lstarestas = list(chunks(lstarestas,2))
print(lstarestas)


'''
output>>>
[['1', '3'], ['1', '7'], ['1', '11'], ['1', '15'], ['1', '19'], ['3', '5'], ['7', '9'], ['11', '13'], ['15', '17'], ['19', '21']]

'''
            
    