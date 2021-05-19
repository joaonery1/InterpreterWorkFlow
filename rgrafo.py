# Python program for 
# validation of a graph
  
# import dictionary for graph
from collections import defaultdict
  
# function for adding edge to graph
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
  
# definition of function
def generate_edges(graph):
    edges = []
  
    # for each node in graph
    for node in graph:
          
        # for each neighbour node of a single node
        for neighbour in graph[node]:
              
            # if edge exists then append
            edges.append((node, neighbour))
    return edges


parametro = defaultdict(list)
def addParam(parametro,input,output):
        parametro[input].append[output]


def gerar_param(parametro):
        lista_parametro = []

        for i in parametro:
                for j in parametro[i]:
                        lista_parametro.append((i,j))
        return lista_parametro


# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

addParam(parametro,"i","o")
# Driver Function call 
# to print generated graph
print(generate_edges(graph)) 