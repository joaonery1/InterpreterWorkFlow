
class Grafo:
    def __init__(self,direcionado= True):
        self.lista_vertices = []
        self.lista_arestas = []
    
    def novo_vertice(self,identificador):
        self.lista_vertices.append(Vertice(identificador))
    
    def busca_aresta(self,u,v):
        for w in self.lista_arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_vertice(self,identificador):
        for i in self.lista_vertices:
            if identificador == i.getId():
                return i 
            else:
                return None
    
    def nova_aresta(self,origem,destino,img_entrada,img_saida):
        origem_aux = self.busca_vertice(origem)
        destino_aux = self.busca_vertice(destino)
        img_entrada_aux = self.busca_vertice(origem)
        img_saida_aux = self.busca_vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_arestas.append(Aresta(origem_aux,destino_aux,img_entrada,img_saida))
        else:
            print("errado")
            
    def imprime_grafo(self,origem,destino):
        if origem == destino:
            print("fim")
        else:
            destino_aux = self.busca_vertice(destino)
            if len(destino_aux.ant) == 0:
                print("erro")
            else:
                print(destino_aux.ant[0])
                self.imprime_grafo(origem,destino_aux.ant[0])
class Vertice():
    def __init__(self,id):
        self.id = id
        self.input = 0
        self.output = 0
        self.ant = []

    def setId(self,id):
        self.id = id
    def getId(self):
        return self.id

    def setInput(self,inp):
        self.input = inp

    def setOutput(self,out):
        self.output = out
   
#    def __str__(self):
#         return (" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): " % (
#      self.id, self.estimativa, self.input, self.output))  # imprimir o predecesso

class Aresta:
    def __init__(self,origem,destino,img_entrada,img_saida):
        self.origem = origem
        self.destino = destino
        self.img_entrada = img_entrada
        self.img_saida = img_saida
    
    def getOrigem(self):
        return self.origem
    
    def getDestino(self):
        return self.destino
    
    def setEntrada(self,img_entrada):
        self.img_entrada = img_entrada
    def getEntrada (self):
        return self.img_entrada
    
    def setSaida(self,img_saida):
        self.img_saida = img_saida
    
    def getSsaida(self):
        return self.img_saida


grafo = Grafo(direcionado=True)
grafo.novo_vertice(1)
grafo.imprime_grafo(1,2)
