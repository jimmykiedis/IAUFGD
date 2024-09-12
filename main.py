import time
import pygame
from copy import deepcopy                       #importar o deepcopy da biblioteca copy para poder fazer uma copia da matriz e poder mexer nela a vontade

def checkWinner(board):
    
def isFull(board):

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

def minimax(board, jogador, eu, maxdepth=9):
    w = checkWinner(board)                      #w recebe da funcao chegckwinner se alguém ganhou
    if w == eu:                                 #se a IA vencer ela recebe 1
        return 1                                
    elif w != eu and not isFull(board):         #se a IA perder ela ela perde 1
        return -1
    elif isFull(board):                         #se der empate ela não recebe nada e ne perde nada
        return 0

def bestAction(board, eu):                      #retorna a melhor jogada
    jogadas = jogadasPossiveis(board)           #recebe a lista de todas as jogadas possiveis
    best = -float('inf')                        #Inicializar o valor infinito negativo, assim, qualquer valor recebido por ele vai ser maior e assim este será substituido
    bestAct = None                              #inicia a melhor ação sem nenhuma valor
    for jogada in jogadas:                      #percorre todas as jogadas possiveis de jogada em jogada
        resultado = resultJogada(board, jogadas[jogada], eu)    #chama a computação de resultados e passa como parametro o tabuleiro, a lista de jogadas possiveis e se o jogador é x ou o
        valor = minimax(board, eu, eu)          #valore drecebera o resultado de minimax que recebe como parametro onde o X ou O foi jogada
        if valor > best:                        #se valor recebido do minimax é maior que melhor(o que é lógico) então...
            best = valor                        #as melhor recebe o minimax
            bestAct = jogadas[jogada]           #e a melhor ação recebe a lista na posição atual do laço
    return bestAct   
#teste
