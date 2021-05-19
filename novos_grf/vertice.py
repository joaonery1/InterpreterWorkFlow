class Vertice():
    def __init__(self,id):
        self.id = id
        self.input = 0
        self.output = 0

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

