class Vertice:
    def __init__(self, idx) : # Constructor   
        """
        id : Integer (1, 2, 3, ..., 81)
        """
        self.id = idx
        self.vizinhos = dict()
        self.valor = 0
    def adiciona_vizinho(self, vizinho) :
        """
        vizinho : vértice

        adiciona o id do vizinho
        """
        if vizinho.id not in self.vizinhos.keys() :  
            self.vizinhos[vizinho.id] = 0
    #getter
    def getVizinhos(self) : 
        return self.vizinhos.keys()

    def getID(self) : 
        return self.id
    
    def set_valor(self, valor_inserido):
        self.valor = valor_inserido
    def getValor(self):
        
        return self.valor
    
    