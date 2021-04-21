def cria_grafo(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])        
    return grafo        

lista_de_arestas = [[1, 3], [1, 7], [1, 11], [1, 15], [1, 19], [3, 3], [3, 15], [5, 3], [7, 9], [11, 13], [17, 3], [19, 21]]
lista_de_vertices = [1, 3, 5, 7, 11, 17, 19]
grafo = cria_grafo(lista_de_vertices, lista_de_arestas)
print(grafo)