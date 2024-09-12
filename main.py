from copy import deepcopy                       #importar o deepcopy da biblioteca copy para poder fazer uma copia da matriz e poder mexer nela a vontade
import time
import pygame

def checkWinner(board):                         #verifica se alguém ganhou

def isFull(board):                              #verifica se o tabuleiro está cheio, ou seja, empate

def heuristica(board, jogador):                 #estima valor do tabuleiro

def resultJogada(board, pos, jogador):          #computa resultado da jogada
    new_board = deepcopy(board)
    new_board[pos[0]][pos[1]] = jogador         #marcar cordenada onde o jogador marcou sua jogada
    return new_board
    
def jogadasPossiveis(board):                    #lista de jogadas possiveis
    jogadas = []                                #criação da lista que acrecentaremos cada espaço vazio como uma possivel jogada
    for linha in range (0,3):                   #testa as linhas
        for coluna in range (0,3):              #testa as colunas de cada linha
            if board[linha][coluna] == None:    #se a posição estiver vazia então...
                jogadas.append([linha,coluna])  #adiciona a lista
    return jogadas                              #aqui estamos retornando todas posições vazias no tabuileiro para ver todas as jogadas possiveis

def minimax(board, jogador, eu, maxdepth=9):    #minimax é um algoritmo da IA, aqui ela montará seu score
    jogadas = jogadasPossiveis(board)           #precisa das jogadas possiveis para o minimax poder calcular qual é a melhor
    w = checkWinner(board)                      #w recebe da funcao chegckwinner se alguém ganhou
    
    if w == eu:                                 #se a IA vencer ela ganha 1 no caso de winner ser 'eu'
        return 1                                
    elif w and w != eu:                         #se a IA perder ela ela perde 1 no caso de haver winner, mas esse não ser 'eu'
        return -1
    elif not w and isFull(board):               #se der empate ela não recebe nada e nem perde nada no caso de não haver vencedor e o tabuleiro estiver cheio
        return 0
    elif maxdepth == 0:
        return heuristica(board, jogador)       #se eu for muito fundo no minimax ele para a recursão e chama a euristica do tabuleiro com o jogador atual pra resolver

    if jogador == eu:                           #Max
        best = -float('inf')                    #percorreremo todas as possiblidades a partir do tabuleiro atual e retornar o valor da maior delas por isso o -infinito
        for jogada in jogadas:                  #o laço de repetição vai em jogada por jogada para testar o maior valor
            resultado = resultJogada(board, jogadas[jogada], jogador)       #resultado guarda a jogada feita em resultJogada()
            valor = minimax(resultado, 'O' if jogador == 'X' else 'X', eu, maxdepth-1)  #qual o valor do tabuleiro depois de fazer a jogada que está dentro de resultJogada()
            if valor > best:                                                #se o valor atual for maior do que o a maior até o momento então...
                best = valor                                                #o maior valor vira o atual
        '''aqui preciso terminar de fazer, deve esta em mais ou menos 30 min de aula e preciso dormir'''
        return best                                                         #retornamos o maior valor para o max
    else:                                       #Min
        best = float('inf')                     #agora faremo o contrário, pegamos o infinito positivo e verificamos os menores valores possiveis para substituir
        for jogada in jogadas:                  #o laço para ver todas as jogadas
            resultado = resultJogada(board, jogadas[jogada], jogador)       #resultado verifica a jogada
            valor = minimax(resultado, 'O' if jogador == 'X' else 'X', eu, maxdepth-1)  #valor pega o resultado da jogada anterior e passa ela pro minimax
            if valor < best:                                                #se o valor que passou pelo minimax for menor que o atual então...
                best = valor                                                #o menor valor agora é o atual
        return best                                                         #retornamos a melhor jogada de menor valor
        
def bestAction(board, eu):                      #retorna a melhor jogada
    jogadas = jogadasPossiveis(board)           #recebe a lista de todas as jogadas possiveis
    best = -float('inf')                        #Inicializar o valor infinito negativo, assim, qualquer valor recebido por ele vai ser maior e assim este será substituido
    bestAct = None                              #inicia a melhor ação sem nenhuma valor
    
    for jogada in jogadas:                      #percorre todas as jogadas possiveis de jogada em jogada
        resultado = resultJogada(board, jogadas[jogada], eu)            #chama a computação de resultados e passa como parametro o tabuleiro, a lista de jogadas possiveis e se o jogador é x ou o
        valor = minimax(resultado, 'O' if eu == 'X' else 'X', eu, 4)    #valor recebido de 'resultado' passa agora pelo minimax que recebe como parametro onde o X ou O foi jogada e tambem a profundidade d pesquisa, quando chegar a zero ele começa a usar a heuristica.
        if valor > best:                        #se valor recebido do minimax é maior que melhor(o que é lógico) então...
            best = valor                        #as melhor recebe o minimax
            bestAct = jogadas[jogada]           #e a melhor ação recebe a lista na posição atual do laço
    return bestAct   
#teste
