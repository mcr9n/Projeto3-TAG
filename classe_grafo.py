from classe_vertice import Vertice
class Grafo:
    #total de vértices no grafo
    total_de_vertices = 0
    
    def __init__(self) : 
        """
        todos_os_nos = Dictionary (key:value)
                   idx : vértice
        """
        self.todos_os_nos = dict()
    def adiciona_vertice(self, idx) : 
        """ cria o nó """
        if idx in self.todos_os_nos : 
            return None
        
        Grafo.total_de_vertices += 1
        vertice = Vertice(idx)
        self.todos_os_nos[idx] = vertice
        return vertice
    def adiciona_aresta(self, src, dst) : 
        """
        adiciona aresta entre dois nós.
        Grafo bidirecionado

        src = origem da aresta
        dst = destino da aresta

        """
        self.todos_os_nos[src].adiciona_vizinho(self.todos_os_nos[dst])
        self.todos_os_nos[dst].adiciona_vizinho(self.todos_os_nos[src])
        
    def eh_vizinho(self, u, v) : 
        """
        checa se esse vizinho existe ou não
        """
        if u >=1 and u <= 81 and v >=1 and v<= 81 and u !=v : 
            if v in self.todos_os_nos[u].getVizinhos() : 
                return True
        return False
    def getVertice(self, idx) : 
        if idx in self.todos_os_nos : 
            return self.todos_os_nos[idx]
        return None

    def getTodosIds(self) : 
        return self.todos_os_nos.keys()
