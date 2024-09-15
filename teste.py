from copy import deepcopy                       # Importar o deepcopy da biblioteca copy para poder fazer uma cópia da matriz e poder mexer nela à vontade
from math import pow                            # Importar potenciação para calcular valores e fazer estimativa da heurística
import pygame
import time

pygame.init()

largura, altura = 610, 610
fonte = pygame.font.Font(None, 120)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('TicTacToeAB')

tamanhoQuadrado = 200
margem = 10

def finalizar():
    pygame.quit()
    exit()

def desenharTabuleiro(board):
    tela.fill(PRETO)
    for linha in range(3):
        for coluna in range(3):
            x = coluna * tamanhoQuadrado + margem
            y = linha * tamanhoQuadrado + margem
            pygame.draw.rect(tela, BRANCO, (x, y, tamanhoQuadrado - margem, tamanhoQuadrado - margem))
            if board[linha][coluna] == 'X':
                texto = fonte.render('X', True, VERMELHO)
                tela.blit(texto, (x + 50, y + 20))
            elif board[linha][coluna] == 'O':
                texto = fonte.render('O', True, AZUL)
                tela.blit(texto, (x + 50, y + 20))

def checkWinner(board):                         # Verifica se alguém ganhou
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:   # Vamos testar cada linha da matriz
            return board[i][0]                  # Retorna quem venceu nessa linha, seja 'X' ou 'O'
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:  # Vamos testar cada coluna da matriz
            return board[0][i]                  # Retorna quem venceu nessa coluna, se 'X' ou 'O'
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:   # Vamos testar a primeira diagonal
        return board[0][0]                      # Retorna quem venceu na diagonal 
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:   # Vamos testar a segunda diagonal
        return board[0][2]                      # Retorna quem venceu na outra diagonal
    return None                                 # Ninguém venceu ainda 

def isFull(board):                              # Verifica se o tabuleiro está cheio, ou seja, empate
    for linha in board:                         # Para cada linha no tabuleiro
        for coluna in linha:                    # Para cada coluna das linhas
            if coluna is None:                  # Se pelo menos uma for vazia então...
                return False                    # É falso, não está cheio
    return True                                 # Se não sair retornar dentro do laço de repetição então ele é verdadeiro, e não há um elemento vazio na matriz

def heuristica(board, jogador):                 # Estima valor do tabuleiro
    h = 0                                       # Inicia-se o valor zerado para que eu possa fazer o valor da minha heurística
    oponente = 'O' if jogador == 'X' else 'X'   # Oponente recebe O, se for a vez do O então o jogador recebe X, se não for, oponente recebe X
    
    for i in range(3):
        if board[i][0] != oponente and board[i][1] != oponente and board[i][2] != oponente: # Se o oponente não fechou nenhuma das chances de vitória pela horizontal então...
            h += pow((board[i][0] == jogador) + (board[i][1] == jogador) + (board[i][2] == jogador), 2) # Incrementa um valor (potencializado) se tiver alguma casa marcada na horizontal
    
    for i in range(3):
        if board[0][i] != oponente and board[1][i] != oponente and board[2][i] != oponente: # Se o oponente não fechou nenhuma das chances de vitória pela vertical então...
            h += pow((board[0][i] == jogador) + (board[1][i] == jogador) + (board[2][i] == jogador), 2) # Incrementa, se tiver chance de ganhar pela vertical
    
    if board[0][0] != oponente and board[1][1] != oponente and board[2][2] != oponente:
        h += pow((board[0][0] == jogador) + (board[1][1] == jogador) + (board[2][2] == jogador), 2)     # Continua incrementando se as jogadas forem na diagonal também
    
    if board[0][2] != oponente and board[1][1] != oponente and board[2][0] != oponente:
        h += pow((board[0][2] == jogador) + (board[1][1] == jogador) + (board[2][0] == jogador), 2)     # Tanto a diagonal esquerda-direita quanto a inversa

    # Faremos o cálculo contrário em caso de desvantagem
    for i in range(3):
        if board[i][0] != jogador and board[i][1] != jogador and board[i][2] != jogador: # Se o oponente não fechou nenhuma das chances de vitória pela horizontal então...
            h -= pow((board[i][0] == oponente) + (board[i][1] == oponente) + (board[i][2] == oponente), 2) # Ele decrementa um valor (potencializado) se tiver alguma casa marcada na horizontal
    
    for i in range(3):
        if board[0][i] != jogador and board[1][i] != jogador and board[2][i] != jogador: # Se o oponente não fechou nenhuma das chances de vitória pela vertical então...
            h -= pow((board[0][i] == oponente) + (board[1][i] == oponente) + (board[2][i] == oponente), 2) # Decrementa, se tiver chance de ganhar pela vertical
    
    if board[0][0] != jogador and board[1][1] != jogador and board[2][2] != jogador:
        h -= pow((board[0][0] == oponente) + (board[1][1] == oponente) + (board[2][2] == oponente), 2)     # Continua decrementando se as jogadas forem na diagonal também
    
    if board[0][2] != jogador and board[1][1] != jogador and board[2][0] != jogador:
        h -= pow((board[0][2] == oponente) + (board[1][1] == oponente) + (board[2][0] == oponente), 2)     # Tanto a diagonal esquerda-direita quanto a inversa

    return h
        
def resultJogada(board, pos, jogador):          # Computa resultado da jogada
    new_board = deepcopy(board)
    new_board[pos[0]][pos[1]] = jogador         # Marca a coordenada onde o jogador marcou sua jogada
    return new_board
    
def jogadasPossiveis(board):                    # Lista de jogadas possíveis
    jogadas = []                                # Criação da lista que acrescentaremos cada espaço vazio como uma possível jogada
    for linha in range(3):                      # Testa as linhas
        for coluna in range(3):                 # Testa as colunas de cada linha
            if board[linha][coluna] is None:    # Se a posição estiver vazia então...
                jogadas.append([linha, coluna]) # Adiciona a lista
    return jogadas                              # Aqui estamos retornando todas as posições vazias no tabuleiro para ver todas as jogadas possíveis

def minimax(board, jogador, eu, alpha, beta, maxdepth=9):    # Minimax é um algoritmo da IA, aqui ela montará seu score
    jogadas = jogadasPossiveis(board)           # Precisa das jogadas possíveis para o minimax poder calcular qual é a melhor
    w = checkWinner(board)                      # w recebe da função checkWinner se alguém ganhou
    
    if w == eu:                                 # Se a IA vencer ela ganha 999 no caso de winner ser 'eu'
        return 999                              # 999 é pra garantir que "o programa entenda" que usar heurística que "é achar que vai ganhar" é incerteza, mas aqui é a certeza, ou seja, é maior. 
    elif w and w != eu:                         # Se a IA perder ela ela perde 999 no caso de haver winner, mas esse não ser 'eu'
        return -999                             # Aqui é o efeito contrário, pro programa entender que é certeza a derrota
    elif not w and isFull(board):               # Se der empate ela não recebe nada e nem perde nada no caso de não haver vencedor e o tabuleiro estiver cheio
        return 0
    elif maxdepth == 0:
        return heuristica(board, jogador)       # Se eu for muito fundo no minimax ele para a recursão e chama a heurística do tabuleiro com o jogador atual pra resolver

    if jogador == eu:                           # Max
        best = -float('inf')                    # Percorreremo todas as possibilidades a partir do tabuleiro atual e retornar o valor da maior delas por isso o -infinito
        for jogada in jogadas:                  # O laço de repetição vai em jogada por jogada para testar o maior valor
            resultado = resultJogada(board, jogada, jogador) # Resultado guarda a jogada feita em resultJogada()
            valor = minimax(resultado, 'O' if jogador == 'X' else 'X', eu, alpha, beta, maxdepth-1)  # Qual o valor do tabuleiro depois de fazer a jogada que está dentro de resultJogada()
            best = max(best, valor)                                         # Usando uma função do python para retornar o valor maximizado
            alpha = max(alpha, best)                                        # Vamos pegar o maior valor entre alpha e best
            if beta <= alpha:                                               # Se o valor atual for maior do que a maior até o momento então...
                break                                                       # Aqui a gente poda valores menores valores das outros galhos da árvore que são subsequentes
        return best                                                         # Se não houver a poda, retorna a máxima
    else:                                       # Min
        best = float('inf')                     # Agora faremos o contrário, pegamos o infinito positivo e verificamos os menores valores possíveis para substituir
        for jogada in jogadas:                  # O laço para ver todas as jogadas
            resultado = resultJogada(board, jogada, jogador)       # Resultado verifica a jogada
            valor = minimax(resultado, 'O' if jogador == 'X' else 'X', eu, alpha, beta, maxdepth-1)  # Valor pega o resultado da jogada anterior e passa ela pro minimax
            best = min(best, valor)                                         # A melhor agora recebe o valor mínimo
            beta = min(beta, best)                                          # O beta agora vai receber o valor mínimo entre o valor atual e a melhor jogada
            if beta <= alpha:                                               # Se o valor que passou pelo minimax for menor que o atual então...
                break                                                       # Vamos podar os valores menores aqui durante a mínima também    
        return best                                                         # Se não haver poda, a gente retorna a mínima
        
def bestAction(board, eu):                      # Retorna a melhor jogada
    jogadas = jogadasPossiveis(board)           # Recebe a lista de todas as jogadas possíveis
    best = -float('inf')                        # Inicializar o valor infinito negativo, assim, qualquer valor recebido por ele vai ser maior e assim este será substituído
    bestAct = None                              # Inicia a melhor ação sem nenhum valor
    
    for jogada in jogadas:                      # Percorre todas as jogadas possíveis de jogada em jogada
        resultado = resultJogada(board, jogada, eu) # Chama a computação de resultados e passa como parâmetro o tabuleiro, a lista de jogadas possíveis e se o jogador é X ou O
        valor = minimax(resultado, 'O' if eu == 'X' else 'X', eu, -float('inf'), float('inf'), 3) # Valor recebido de 'resultado' passa agora pelo minimax que recebe como parâmetro onde o X ou O foi jogada e também a profundidade da pesquisa, quando chegar a zero ele começa a usar a heurística
        if valor > best:                        # Se valor recebido do minimax é maior que melhor(o que é lógico) então...
            best = valor                        # A melhor recebe o minimax
            bestAct = jogada                    # E a melhor ação recebe a lista na posição atual do laço
    return bestAct

def jogo():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]
    ]

    jogadorAtual = 'X'
    jogando = True
    vencedor = None

    while jogando:
        desenharTabuleiro(board)
        pygame.display.flip()
        
        if jogadorAtual == 'O':  # A IA joga como 'O'
            time.sleep(1)  # Para dar um pequeno delay e ver a jogada da IA
            jogada = bestAction(board, 'O')
            if jogada is not None:
                board[jogada[0]][jogada[1]] = 'O'
                vencedor = checkWinner(board)
                if vencedor:
                    print(f'O jogador {vencedor} venceu!')
                elif isFull(board):
                    print(f'Empate')
                jogadorAtual = 'X'
        else:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jogando = False
                    finalizar()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        finalizar()

                if evento.type == pygame.MOUSEBUTTONDOWN and vencedor is None:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    
                    linha = mouseY // tamanhoQuadrado
                    coluna = mouseX // tamanhoQuadrado

                    if board[linha][coluna] is None:
                        board[linha][coluna] = jogadorAtual

                        vencedor = checkWinner(board)

                        if vencedor:
                            print(f'O jogador {vencedor} venceu!')
                        elif isFull(board):
                            print(f'Empate')

                        jogadorAtual = 'O' if jogadorAtual == 'X' else 'X'

        if vencedor or isFull(board):
            tela.fill(PRETO)
            textoFinal = fonte.render(f'{vencedor} venceu' if vencedor else 'Empate!', True, BRANCO)
            tela.blit(textoFinal, (200, 250))
            pygame.display.flip()
            time.sleep(4)
            jogando = False
            finalizar()

    pygame.quit()

jogo()
