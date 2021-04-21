class ArquivoGraph(object):
    nomaArq = "nodeconnections.wk"
    arquivo = nomaArq

    def __init__(self, nomaArq):
        self.nomaArq = nomaArq
        self.arquivo = open(self.nomaArq + ".txt", "w")
        self.arquivo.write("digraph G {\n")
    
    def addAresta(self, v1, v2, relacao):
        self.arquivo.write(v1 + " -- " + v2 + " [ label= " + relacao + " ]\n")
    
    def add(self, v1, v2):
        self.arquivo.write(v1 + " -- " + v2 +"\n")
    
    def addVertice(self, v1):
        self.arquivo.write(v1 +"\n")
    
    def escreveGrafo(self, grafo):
        vertices = grafo.vertices
        escritos = {}
        for elmento in vertices:
            escritos[elmento] = {}
            for elmento2 in vertices:
                escritos[elmento][elmento2] = False
        
        for chave in vertices:
            chavesVizinhos = grafo.getVizinhos(chave)
            for chaveVizinho in chavesVizinhos:
                if(not escritos[chave][chaveVizinho] and not escritos[chaveVizinho][chave]):
                    self.arquivo.write(str(chave) + " -- " + str(chaveVizinho))
                    self.arquivo.write(" [ label= " + str(grafo.retornaRelacao(chave, chaveVizinho)) + " ]\n")
                    escritos[chave][chaveVizinho] = True
    
    def escreveGrafoDirecionado(self, grafo):
        vertices = grafo.vertices
        escritos = {}
        for elmento in vertices:
            escritos[elmento] = {}
            for elmento2 in vertices:
                escritos[elmento][elmento2] = False
        
        for chave in vertices:
            chavesVizinhos = grafo.getVizinhos(chave)
            for chaveVizinho in chavesVizinhos:
                if(not escritos[chave][chaveVizinho] and not escritos[chaveVizinho][chave]):
                    self.arquivo.write(str(chave) + " -> " + str(chaveVizinho))
                    self.arquivo.write(" [ label= " + str(grafo.retornaRelacao(chave, chaveVizinho)) + " ]\n")
                    escritos[chave][chaveVizinho] = True
        
        
    def close(self):
        self.arquivo.write('}')
        self.arquivo.close()



arestas = [[1, 3], [1, 7], [1, 11], [1, 15], [1, 19], [3, 3], [3, 15], [5, 3], [7, 9], [11, 13], [17, 3], [19, 21]]
grafo = (arestas,"nodeconnections.wk")
print("Saida da lista de nodes:")

print("Saida do grafo:")

print("Saida das arestas:")

print("Saida dos vertices:")
