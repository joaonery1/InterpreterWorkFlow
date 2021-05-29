
#classe teste
import os
def lerWork(lstu,lstout,lstinp):
    if os.path.isfile("interpreterworkflow.wk"):
        file1 = open("interpreterworkflow.wk","r")
        for line in file1:
            if 'nodeconnection' in line.lower():
                conexao = line.split(':')
                lstu.append(conexao[2])
                lstu.append(conexao[4])
                lstinp.append(conexao[5])
                lstout.append(conexao[3])
                print(conexao)
        file1.close()

lstarestas = []
lstout = []
lstv = []
lstinp = []
lerWork(lstarestas,lstout,lstinp)
print(lstarestas,lstout,lstinp)