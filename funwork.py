
import re
import os
import string

# -*- coding: utf-8 -* 
from collections import defaultdict

class objGlyph(object):
    def __init__(self, vglyph_id,):       
        self.vglyph_id = vglyph_id      

    def __repr__(self):
        return "{}".format(self.vglyph_id)

class objConnection(object):

    def __init__(self,u_id,u_output,v_id,v_input):
        self.u_id= u_id
        self.u_output = u_output
        self.v_id = v_id
        self.v_input = v_input
    
    def __repr__(self):
        return "{},{}".format(self.u_output,self.v_input)

    #funcao para criar sub-listas
    def chunks(self,lista,n):
        for i in range(0,len(lista),n):
            yield lista[i:i +n]
        return lista

    #funcao para remover itens repetidos de uma lista
    def remove_repetidos(self,lista):
        l = []
        for i in lista:
         if i not in l:
            l.append(i)
        return l

lstConnection = []
lstGlyph = []
vConnection = objConnection
vGlyph = objGlyph



#ideia de leitura com parametros
def connection_parameters(lstGlyph):
    if os.path.isfile("arquivos.wk/data.wksp"):
        file1 = open("arquivos.wk/data.wksp","r")
        
        for line in file1:
            if 'glyph:' in line.lower():
                conexao = line.split(':')
                vGlyph = objGlyph(conexao[5])
                lstGlyph.append(vGlyph)

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
lstvetx = []
lstvertex = []
connection_parameters(lstGlyph)
for vConnection in lstConnection:
    lstedge.append(vConnection.u_id)
    lstparam.append(vConnection.u_output)
    lstedge.append(vConnection.v_id)
    lstparam.append(vConnection.v_input)
    #print(vConnection.u_id,vConnection.v_id)

lstPout = []
lstPinp = []
for vConnection in lstConnection:
    lstPinp.append(vConnection.v_input)
    lstPout.append(vConnection.u_output)


for val in lstedge:
    lstedges.append(int(val))

for vGlyph in lstGlyph:
    lstvetx.append(vGlyph.vglyph_id)

for val1 in lstvetx:
    lstvertex.append(int(val1))



print("####################################")

lstcomplete= [*sum(zip(lstedges,lstparam),())]    #juntei depois de alimentar a lista
lstcomplete = list(vConnection.chunks(lstcomplete,4))
lstedges = list(vConnection.chunks(lstedges,2))
lstvertex = vConnection.remove_repetidos(lstvertex)
print("Lista de vertices:\n",lstvertex,"\n")   #lista de vertices 
print(lstedges,"\n") #lista de arestas
print(lstcomplete,"\n") #lista arestas c/ parametros
print("Parametros de saida:" ,lstPout)
print("Parametros de entrada:" ,lstPinp)

print("####################################")
'''
'''