from classe_grafo import Grafo
from classe_vertice import Vertice
class conexoes_do_sudoku:
    
    def __init__(self) :  # construtor

        self.grafo = Grafo() # Objeto grafo

        self.linhas = 9
        self.colunas = 9
        self.total_de_celulas = self.linhas*self.colunas #81

        self.gera_grafo() # Gera todos os vértices
        self.conecta_arestas() # conecta todos os vértices de acordo com o padrão do sudoku

        self.todos_os_ids = self.grafo.getTodosIds() # coloca todos os ids em uma lista
    def gera_grafo(self) : 
        """
        gera vértices com ids de 1 até 81.
        """
        for idx in range(1, self.total_de_celulas+1) : 
            _ = self.grafo.adiciona_vertice(idx)
    def gera_matriz_guia(self) : 
        """
        Gera uma matriz com os possíveis ids.
        
        Mapeia cada célula com um vértice por meio dos ids
        """
        matriz = [[0 for colunas in range(self.colunas)] 
        for colunas in range(self.colunas)]

        contador = 1
        for linhas in range(9) :
            for colunas in range(9):
                matriz[linhas][colunas] = contador
                contador+=1
        return matriz
    def o_que_conectar(self, matriz, linhas, colunas) :

        """
        matriz : guarda o id de cada vértice na determinada célula

        retorna dicionário

        conexoes -> dicionário
        linhas : [todos os ids nas respectivas linhas]
        colunas : [todos os ids nas respectivas colunas]
        blocos : [todos os ids nos respectivos blocos]
        
        ** a serem conectados com o alvo.
        """
        conexoes = dict()

        linha = []
        coluna = []
        bloco = []

        # LINHAS
        for c in range(colunas+1, 9) : 
            linha.append(matriz[linhas][c])
        
        conexoes["linhas"] = linha

        # COLUNAS 
        for r in range(linhas+1, 9):
            coluna.append(matriz[r][colunas])
        
        conexoes["colunas"] = coluna

        # BLOCOS
        
        if linhas%3 == 0 : 

            if colunas%3 == 0 :
                
                bloco.append(matriz[linhas+1][colunas+1])
                bloco.append(matriz[linhas+1][colunas+2])
                bloco.append(matriz[linhas+2][colunas+1])
                bloco.append(matriz[linhas+2][colunas+2])

            elif colunas%3 == 1 :
                
                bloco.append(matriz[linhas+1][colunas-1])
                bloco.append(matriz[linhas+1][colunas+1])
                bloco.append(matriz[linhas+2][colunas-1])
                bloco.append(matriz[linhas+2][colunas+1])
                
            elif colunas%3 == 2 :
                
                bloco.append(matriz[linhas+1][colunas-2])
                bloco.append(matriz[linhas+1][colunas-1])
                bloco.append(matriz[linhas+2][colunas-2])
                bloco.append(matriz[linhas+2][colunas-1])

        elif linhas%3 == 1 :
            
            if colunas%3 == 0 :
                
                bloco.append(matriz[linhas-1][colunas+1])
                bloco.append(matriz[linhas-1][colunas+2])
                bloco.append(matriz[linhas+1][colunas+1])
                bloco.append(matriz[linhas+1][colunas+2])

            elif colunas%3 == 1 :
                
                bloco.append(matriz[linhas-1][colunas-1])
                bloco.append(matriz[linhas-1][colunas+1])
                bloco.append(matriz[linhas+1][colunas-1])
                bloco.append(matriz[linhas+1][colunas+1])
                
            elif colunas%3 == 2 :
                
                bloco.append(matriz[linhas-1][colunas-2])
                bloco.append(matriz[linhas-1][colunas-1])
                bloco.append(matriz[linhas+1][colunas-2])
                bloco.append(matriz[linhas+1][colunas-1])

        elif linhas%3 == 2 :
            
            if colunas%3 == 0 :
                
                bloco.append(matriz[linhas-2][colunas+1])
                bloco.append(matriz[linhas-2][colunas+2])
                bloco.append(matriz[linhas-1][colunas+1])
                bloco.append(matriz[linhas-1][colunas+2])

            elif colunas%3 == 1 :
                
                bloco.append(matriz[linhas-2][colunas-1])
                bloco.append(matriz[linhas-2][colunas+1])
                bloco.append(matriz[linhas-1][colunas-1])
                bloco.append(matriz[linhas-1][colunas+1])
                
            elif colunas%3 == 2 :
                
                bloco.append(matriz[linhas-2][colunas-2])
                bloco.append(matriz[linhas-2][colunas-1])
                bloco.append(matriz[linhas-1][colunas-2])
                bloco.append(matriz[linhas-1][colunas-1])
        
        conexoes["blocos"] = bloco
        return conexoes
    def conecta_tais(self, conexoes_de_alvo) : 
        for alvo in conexoes_de_alvo.keys() : #alvo é o idx inicial
            conexoes = conexoes_de_alvo[alvo]
            for key in conexoes :  #pega cada uma das listas de conexões necessárias
                for v in conexoes[key] : 
                    self.grafo.adiciona_aresta(alvo, v)
    def conecta_arestas(self) : 
        """
        conecta vértices de acordo com o padrão do sudoku : 

        # linhas

       tendo como início cada número de id, conecte todos os números sucessores,
       até que você atinja um múltiplo de 9.


        # colunas (+9)

        tendo como início cada número de id. +9 para cada conexão
        até que você atinja um número >= 73 e <= 81

        # blocos
        conecta dos os elementos do bloco que não estão na mesma linha ou coluna.
        1   2   3
        10  11  12
        19  20  21

        1 -> 11, 12, 20, 21
        2 -> 10, 19, 12, 21
        3 -> 10, 11, 19, 20 

        """
        matriz = self.gera_matriz_guia()

        conexoes_de_alvo = dict() # alvo : conexões

        for linha in range(9) :
            for coluna in range(9) : 
                
                alvo = matriz[linha][coluna] #id of the node
                conexoes = self.o_que_conectar(matriz, linha, coluna)
                
                conexoes_de_alvo[alvo] = conexoes
        # conecta todas as arestas

        self.conecta_tais(conexoes_de_alvo)
    
    

    