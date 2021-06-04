# funcao pra adcioanar o vertice

def __init__(self):
  self.add_vertex()

def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print( v, " vertice existe")  #caso o vertice exista
  else:
    vertices_no = vertices_no + 1
    graph[v] = []


# funcao pra adcionar o vertice e o parametro
def add_edge(v1, v2, lista_entrada, lista_saida):
  global graph

  # verificar se o v1 eh valido
  if v1 not in graph:
    print("Vertice ", v1, " não existe.")
  # verificar se o v2 eh valido
  elif v2 not in graph:
    print("Vertice", v2, " nao existe")
  else:
    temp = [v2]
    inputs = [lista_entrada]
    outputs = [lista_saida]
    graph[v1].append(temp)
    graph[v1].append(inputs)
    graph[v1].append(outputs)

def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0])

'''
Dados:1:o:3:i
mediadp:3:o:5:i
media:5:o:i:9
mediadp:3:o1:5:i1
desvio_padrao:7:o:i:11
'''


graph = {}
vertices_no = 0

add_vertex(1)
add_vertex(3)
add_vertex(5)
add_vertex(7)
add_vertex(9)
add_vertex(11)

add_edge(1, 3,'o','i')
add_edge(3, 5, 'o','i')
add_edge(3, 7,'o1','i1')
add_edge(5, 9,'o','i')
add_edge(7,11,'o','i')

print ("Representação", graph)
'''
output
{1: [[1, 'i', 3, 'o']], 3: [[3, 'i', 5, 'o'], [3, 'i1', 7, 'o1']], 
5: [[5, 'i', 9, 'o']], 7: [[7, 'i', 11, 'o']], 9: [], 11: []}
'''

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

lv = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 1, 3, 5, 7, 13, 37, 39, 41, 43, 45, 47, 49, 51, 53, 90, 93]
la = [[1, 13], [3, 5], [3, 7], [3, 1], [3, 13], [5, 7], [5, 1], [7, 1], [11, 5], [13, 9], [1, 3], [3, 5], [3, 39], [5, 7], [5, 53], [7, 33], [7, 31], [9, 37], [11, 9], [13, 11], [15, 9], [15, 13], [17, 15], [19, 9], [19, 17], [21, 19], [23, 25], [25, 9], [25, 21], [27, 9], [27, 
31], [29, 27], [31, 23], [33, 29], [35, 49], [39, 51], [39, 21], [41, 13], [43, 17], [47, 35], [49, 1], [51, 45], [53, 21], [53, 17], [53, 13], [90, 47], [93, 39], [93, 43], [93, 41]]

grafo = Grafo(la,direcionado=False)
print(grafo.adj)
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

# Exemplo de uso
G = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['B', 'C']}
for caminho in gerar_caminhos(G, ['A'], 'D'):
    # "print(caminho)" em python3
    print (caminho)



# Objective: read VGLGui workflow file and load content into memory
# File type: structure.txt

#
import sys
import re
import os
import string
from collections import defaultdict

# Structure for storing Glyphs in memory
class objGlyph(object):
        
    #Glyph:[Library]:comment::localhost:[Glyph_ID]:[Glyph_X]:[Glyph_Y]:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]    
    def __init__(self, vlibrary, vfunc, vlocalhost, vglyph_id, vglyph_x, vglyph_y, vlst_par):       
        self.library = vlibrary       #library name (Ex: VisionGL)
        self.func = vfunc             #function
        self.localhost = vlocalhost   #folder where the image file or library function is located
        self.glyph_id = vglyph_id     #glyph identifier code
        self.glyph_x = vglyph_x       #numerical coordinate of the glyph's linear position on the screen 
        self.glyph_y = vglyph_y       #numerical coordinate of the column position of the Glyph on the screen
        self.lst_par = vlst_par       #parameter list

# Structure for storing Parameters in memory
class objGlyphParameters(object):

    def __init__(self, vglyph_id, vname, vvalue):
        self.glyph_id = vglyph_id   #glyph identifier code
        self.name = vname           #variable name
        self.value = vvalue         #variable value

# Structure for storing Connections in memory
class objConnection(object):

    #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
    def __init__(self, vtype, voutput_glyph_id, voutput_varname, vinput_glyph_id, vinput_varname):       
        self.type = vtype                           #type 'data', 'controle' 
        self.output_glyph_id = voutput_glyph_id     #glyph identifier code output
        self.output_varname = voutput_varname      #nome variável saída
        self.input_glyph_id = vinput_glyph_id       #glyph identifier code input
        self.input_varname = vinput_varname         #nome variável entrada

# File to be read
vfile = 'fileread/data.wksp'

lstGlyph = []                   #List to store Glyphs
lstGlyphPar = []                #List to store Glyphs Parameters
lstConnection = []              #List to store Connections

vGlyph = objGlyph               #Glyph in memory 
vGlyphPar = objGlyphParameters  #Glyp parameters in memory
vConnection = objConnection     #Connection in memory



# Method for reading the workflow file
def fileRead(lstGlyph):
    
    if os.path.isfile(vfile):
        # Opens the workflow file
        try:
            file1 =open(vfile,"r")
        except FileNotFoundError:
            print("Arquivo não encontrado")
        for line in file1:

            # Creates the glyphs of the workflow file
            if 'glyph:' in line.lower():

                contentGly = line.split(':')    #extracts the contents of the workflow file line in a list separated by the information between the ":" character
                contentGlyPar = []              #clears the glyph parameter list
                vparName = ''
                vparValue = ''
                try:
                    contentGly = contentGly[9].split(' ')
                    for vpar in contentGlyPar:
                        if vpar != '' and vpar != '\n':
                            vparName = vpar.replace('-', '')
                            vGlyphPar = objGlyphParameters(contentGly[5], vparName, 'fixo')
                            lstGlyphPar.append(vGlyphPar)
                except:
                    print("Falta algum dado na linha do glifo",sys.exc_info()[0])
                else:
                #Crate the Glyph
                        vGlyph = objGlyph(contentGly[1], contentGly[2], contentGly[4], contentGly[5], contentGly[6], contentGly[7], lstGlyphPar)
                        lstGlyph.append(vGlyph)   

            # Creates the connections of the workflow file
            if 'nodeconnection:' in line.lower():
                contentCon = line.split(':')
                try:
                    vConnection = objConnection(contentCon[1], contentCon[2], contentCon[3], contentCon[4], contentCon[5])
                    lstConnection.append(vConnection)
                except:
                    print("erro")
        file1.close()
      
            
        
      
               


# Program execution
lstGlyph = []
lstConnection = []
contentGly = []
contentCon = []

# Reading the workflow file
fileRead(lstGlyph)

# Shows the content of the Glyphs
for vGlyph in lstGlyph:
    print("Library:", vGlyph.library, "Function:", vGlyph.func, "Localhost:", vGlyph.localhost, "Glyph_Id:", vGlyph.glyph_id, 
          "Position_Line:", vGlyph.glyph_x, "Position_Column:", vGlyph.glyph_y)#, "Parameters:", vGlyph.lst_par)

# Shows the content of the Connections
for vConnection in lstConnection:
    print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
          "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)