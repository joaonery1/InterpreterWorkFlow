import vertice
import aresta


class Grafo:
    def __init__(self,direcionado= True):
        self.lista_vertices = []
        self.lista_arestas = []
    
    def novo_vertice(self,identificador):
        self.lista_vertices.append(vertice(identificador))
    
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
            self.lista_arestas.append(aresta(origem_aux,destino_aux,img_entrada,img_saida))
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