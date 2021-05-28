#importacao 
import re
import string
#declaracao das funcoes
def fun_node(var):
    var = var.split(':')
    var = var[2::]
    lista_entrada = []
    lista_saida = []
    lista_entrada.append(var[3])
    lista_saida.append(var[1])


def fun_duplas(parametros):
    lista = []
    filtro = re.compile('([0-9]+)')
    resp = filtro.findall(parametros)
    for duplas in resp:
        resp = list(map(int,resp))
        lista.append(duplas)   
    num = list(map(int,lista))
    print(num)

#script para leitura do arquivo e aplicao das funcoes
with open('interpreterworkflow.wk') as file:
    for line in file:
        if 'nodeconnection' in line.lower():
            fun_node(line)
            fun_duplas(line)
        elif 'glyph' in line.lower():
            print("existe")
            #funcao para tratar os glyphos e suas variaveis