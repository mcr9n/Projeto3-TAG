from gera_conexoes_sudoku import conexoes_do_sudoku
def matriz_vazia():
    matriz = [
            [0,0,0,0,0,0,0,0,0],        
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
    return matriz
def monta_jogo_inicial():
    '''tabuleiro inicial do sudoku a ser inserido manualmente'''
    tabuleiro = [
            [5,3,0,0,7,0,0,0,0],        
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1], 
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
    return tabuleiro

def coloca_tabuleiro_no_grafo(tabuleiro, grafo):
    '''função que coloca o tabuleiro em forma de matriz em um grafo'''
    contador = 1
    for linha in tabuleiro:
        for elemento in linha:
            grafo.todos_os_nos[contador].valor = elemento
            contador += 1
    return grafo

def resolve_jogo(grafo):
    '''função principal para resolução do jogo usando coloração de grafos, que gera uma matriz com as possibilidades de cada célula'''
    for idx in grafo.todos_os_nos:
        valores_que_tem = []
        if grafo.todos_os_nos[idx].valor == 0:
            
            for vizinho in grafo.todos_os_nos[idx].getVizinhos():
                
                valores_que_tem.append(grafo.todos_os_nos[vizinho].valor)
            lista_de_possibilidades = []
            
            for valor in range(1,10):
                if valor not in valores_que_tem:
                    lista_de_possibilidades.append(valor)
                   
            grafo.todos_os_nos[idx].valor = lista_de_possibilidades
    print()
    print("Matriz de possibilidades após aplicação do algoritmo coloração de grafo")
    print()
    matriz = matriz_vazia()
    matriz = coloca_grafo_no_tabuleiro(matriz,grafo)
    for linha in matriz:
        print(linha)
    contador_de_uns = 0
    while checa_se_tem_listas() != 0:
    
        grafo = constraint_propagation(grafo)
        contador_de_uns += 1
        if contador_de_uns > 100:
            break
    
            
    return grafo

    
def coloca_grafo_no_tabuleiro(matriz,grafo):
    '''função que coloca o grafo em uma matriz para facilitar a exibição da solução final.'''
    contador = 1
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            matriz[linha][coluna] = grafo.todos_os_nos[contador].valor
            contador += 1
    return matriz
def constraint_propagation(grafo):
    '''algoritmo de constraint propagation para geração da solução final apartir da matriz de possibilidades'''
    for idx in grafo.todos_os_nos:
        if isinstance(grafo.todos_os_nos[idx].valor, list): 
            if len(grafo.todos_os_nos[idx].valor) == 1:
                
                valor = grafo.todos_os_nos[idx].valor[0]
                grafo.todos_os_nos[idx].valor = valor
                for vizinho in grafo.todos_os_nos[idx].getVizinhos():
                    if isinstance(grafo.todos_os_nos[vizinho].valor, list):
                        if valor in grafo.todos_os_nos[vizinho].valor:
                            grafo.todos_os_nos[vizinho].valor.remove(valor)
                    
            
    return grafo

    
def checa_se_tem_listas():
    '''checa se ainda tem listas na matriz de possibilidades'''
    for idx in grafo.todos_os_nos:
        if isinstance(grafo.todos_os_nos[idx].valor, list):
            return 1
    return 0

def tabuleiro_invalido(matriz):
    '''verifica se o tabuleiro inserido foi válido e a solução é possível'''
    for i in matriz:
        for elemento in i:
            if isinstance(elemento, list):
                return 1
    return 0
            
            
sudoku = conexoes_do_sudoku()                                #Gera grafo com conexões necessárias para o tabuleiro de sudoku    
tabuleiro = monta_jogo_inicial()                             #Monta tabuleiro(matriz) com o jogo inicial.
print("Tabuleiro Inicial:")
print()
for linha in tabuleiro:                                      #é mostrado o tabuleiro inicial
    print(linha)
grafo = coloca_tabuleiro_no_grafo(tabuleiro, sudoku.grafo)   #coloca o tabuleiro em um grafo
sudoku.grafo = resolve_jogo(sudoku.grafo)                    #resolve jogo proposto usando coloração de grafos para gerar a matriz de possibilidades, em seguida o algoritmo de constraint propagation
matriz = coloca_grafo_no_tabuleiro(tabuleiro, sudoku.grafo)  #coloca o grafo na forma de uma matriz para exibição
tabuleiro_invalido = tabuleiro_invalido(matriz)              #checa se o tabuleiro proposto foi ou não inválido

if tabuleiro_invalido:
    print()
    print("Não há solução porque o tabuleiro inserido é inválido")
else:
    print()
    print("Solução final:")
    print()
    for linha in matriz:
        print(linha)

        
    
        
    
