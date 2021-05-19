class Aresta():
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
    
    def getSsaida(self,img_saida):
        return self.img_saida

    