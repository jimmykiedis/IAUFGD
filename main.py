from copy import deepcopy                           #importar uma biblioteca para fazer uma copia da matriz e poder mexer nela a vontade
from math import pow                                #importa potenciação para que eu possa fazer calcular valores e fazer estimativa da heuristica
import pygame                                       #pra ajudar a abstrair vamos usar o pygame para desenhar o jogo
import time                                         #pra deixar mais dinamico, vamos simular um tempo para a IA pensar

pygame.init()                                       #inicia o pygame pra ajudar a gente a abstrair graficamente

largura, altura = 610, 610                          # algumas constantes 
fonte = pygame.font.Font(None, 120)                 #definindo a fonte que vamos usar, o None é para usar a fonte padrão do pygame, e 120 é o tamanho da fonte    
tamanhoQuadrado = 200
margem = 10

tela = pygame.display.set_mode((largura, altura))   #a definição da tela
pygame.display.set_caption('TicTacToeAB')

def finalizar():                                    #decidi fazer uma função para finalizar o jogo e deixar melhor claro o que fazer caso eu queira fechar a tela do jogo
    pygame.quit()
    exit()

def desenharTabuleiro(tabuleiro):                               #desenhando o tabuleiro com pygame
    tela.fill((0, 0, 0))                                        #completando com a cor preta de fundo
    for linha in range (3):                                     #para cada linha...
        for coluna in range (3):                                #em cada coluna
            x = coluna * tamanhoQuadrado + margem               #definindo o tamanho das colunas
            y = linha * tamanhoQuadrado + margem                #agora o tamanho das linhas
            pygame.draw.rect(tela, (255, 255, 255), (x, y, tamanhoQuadrado - margem, tamanhoQuadrado-margem))   #desenhando o retangulos baseado nos tamanhos e na quantidade de retangulos
            if tabuleiro[linha][coluna] == 'X':                     #para cada iteração, se o retangulo receber 'X'
                texto = fonte.render('X', True, (255, 0, 0))    #ele é desenhado na tela na cor vermelha
                tela.blit(texto, (x + 50, y + 20))              #mais ou menos perto do meio
            elif tabuleiro[linha][coluna] == 'O':                   #para cada iteração, se o retangulo receber 'O'
                texto = fonte.render('O', True, (0, 0, 255))    #desenhamos ele na tela com a cor azul
                tela.blit(texto, (x + 50, y +50))               #tentansmo fazer no mais centrado possivel

def checarVencedor(tabuleiro):                                                             #verifica se alguém ganhou
    for i in range (3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[0][i] is not None:   #vamos testar cada linha da matriz tem tem o mesmo conteúdo, no caso nada
            return tabuleiro[i][0]                                                      #retorna o conteudo que está nessa posição da matriz, quem venceu nessa linha, seja 'X' ou 'O'
    for i in range (3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] is not None:   #vamos testar cada coluna da também
            return tabuleiro[0][i]                                                      #retorna quem venceu nas colunas, se 'x' ou '0'
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] is not None:       #vamos testar a primeira diagonal
        return tabuleiro[0][0]                                                          #retorna quem venceu na diagonal 
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] is not None:       #vamos testar a segunda diagonal
        return tabuleiro[0][2]                                                          #retorna quem venceu na outra diagonal
    return None                                 #ninguém venceu ainda 

def estaCheio(tabuleiro):                       #verifica se o tabuleiro está cheio, ou seja, empate
    for linhas in tabuleiro:                    #para cada linha no tabuleiro
        for colunas in linhas:                  #para cada coluna das linhas
            if colunas is None:                 #se pelo menos uma for vazia então...
                return False                    #é falso, não está cheio
    return True                                 #se não sair retornar dentro do laço de repetição então ele é verdadeiro, e não há um elemento vazio na matriz

def heuristica(tabuleiro, jogador):             #estima valor do tabuleiro
    h = 0                                       #inicia-se o valor zerado para que eu possa fazer o valor da minha heuristica
    oponente = 'O' if jogador == 'X' else 'X'   #oponente recebe O, se for a vez do O então o jogador recebe X, se não for, oponente recebe X
    
    for i in range (3):
        if tabuleiro[i][0] != oponente and tabuleiro[i][1] != oponente and tabuleiro[i][2] != oponente:                 #se o oponente não fechou nenhuma das chances de vitoria pela horizontal então...
            h += pow((tabuleiro[i][0] == jogador) + (tabuleiro[i][1] == jogador) + (tabuleiro[i][2] == jogador), 2)     #ele incrementa um valor(potencializado) se tiver alguma casa marcada na horizontal
    
    for i in range (3):
        if tabuleiro[0][i] != oponente and tabuleiro[1][i] != oponente and tabuleiro[2][i] != oponente:                 #se o oponente não fechou nenhuma das chance de vitoria pela vertical então...
            h += pow((tabuleiro[0][i] == jogador) + (tabuleiro[1][i] == jogador) + (tabuleiro[2][i] == jogador), 2)     #incrimenta, se tiver chance de ganha pela vertical
    
    if tabuleiro[0][0] != oponente and tabuleiro[1][1] != oponente and tabuleiro[2][2] != oponente:
        h += pow((tabuleiro[0][0] == jogador) + (tabuleiro[1][1] == jogador) + (tabuleiro[2][2] == jogador), 2)         #continua incrementando se as jogadas forem na diagonal tbm
    
    if tabuleiro[0][2] != oponente and tabuleiro[1][1] != oponente and tabuleiro[2][0] != oponente:
        h += pow((tabuleiro[0][2] == jogador) + (tabuleiro[1][1] == jogador) + (tabuleiro[2][0] == jogador), 2)         #tanto a diagonal esquerda-direita quanto a inversa

    for i in range (3):                                                                                     #faremos o calculo contrário em caso de desvantagem também
        if tabuleiro[i][0] != jogador and tabuleiro[i][1] != jogador and tabuleiro[i][2] != jogador:                    #se o oponente não fechou nenhuma das chances de vitoria pela horizontal então...
            h -= pow((tabuleiro[i][0] == oponente) + (tabuleiro[i][1] == oponente) + (tabuleiro[i][2] == oponente), 2)  #ele incrementa um valor(potencializado) se tiver alguma casa marcada na horizontal
    
    for i in range (3):
        if tabuleiro[0][i] != jogador and tabuleiro[1][i] != jogador and tabuleiro[2][i] != jogador:                    #se o oponente não fechou nenhuma das chance de vitoria pela vertical então...
            h -= pow((tabuleiro[0][i] == oponente) + (tabuleiro[1][i] == oponente) + (tabuleiro[2][i] == oponente), 2)  #incrimenta, se tiver chance de ganha pela vertical
    
    if tabuleiro[0][0] != jogador and tabuleiro[1][1] != jogador and tabuleiro[2][2] != jogador:
        h -= pow((tabuleiro[0][0] == oponente) + (tabuleiro[1][1] == oponente) + (tabuleiro[2][2] == oponente), 2)      #continua incrementando se as jogadas forem na diagonal tbm
    
    if tabuleiro[0][2] != jogador and tabuleiro[1][1] != jogador and tabuleiro[2][0] != jogador:
        h -= pow((tabuleiro[0][2] == oponente) + (tabuleiro[1][1] == oponente) + (tabuleiro[2][0] == oponente), 2)      #tanto a diagonal esquerda-direita quanto a inversa

    return h
        
def resultJogada(tabuleiro, pos, jogador):                      #computa resultado da jogada
    new_tabuleiro = deepcopy(tabuleiro)
    new_tabuleiro[pos[0]][pos[1]] = jogador                     #marcar cordenada onde o jogador marcou sua jogada
    return new_tabuleiro
    
def jogadasPossiveis(tabuleiro):                                #lista de jogadas possiveis
    jogadas = []                                                #criação da lista que acrecentaremos cada espaço vazio como uma possivel jogada
    for linha in range (3):                                     #testa as linhas
        for coluna in range (3):                                #testa as colunas de cada linha
            if tabuleiro[linha][coluna] == None:                #se a posição estiver vazia então...
                jogadas.append([linha,coluna])                  #adiciona a lista
    return jogadas                                              #aqui estamos retornando todas posições vazias no tabuileiro para ver todas as jogadas possiveis

def minimax(tabuleiro, jogador, eu, alpha, beta, maxdepth=9):   #minimax é um algoritmo da IA, aqui ela montará seu score
    jogadas = jogadasPossiveis(tabuleiro)                       #precisa das jogadas possiveis para o minimax poder calcular qual é a melhor
    w = checarVencedor(tabuleiro)                               #w recebe da funcao chegckwinner se alguém ganhou
    
    if w == eu:                                                 #se a IA vencer ela ganha 999 no caso de winner ser 'eu'
        return 999                                              #999 é pra garantir que a "o programa entenda" que usar heuristica que "é achar que vai ganhar" é incerteza, mas aqui é a certeza, ou seja, é maior. 
    elif w and w != eu:                                         #se a IA perder ela ela perde 999 no caso de haver winner, mas esse não ser 'eu'
        return -999                                             #aqui é o efeito contrário, pro programa entender que é certeza a derrota
    elif not w and estaCheio(tabuleiro):                        #se der empate ela não recebe nada e nem perde nada no caso de não haver vencedor e o tabuleiro estiver cheio
        return 0
    elif maxdepth == 0:
        return heuristica(tabuleiro, jogador)                   #se eu for muito fundo no minimax ele para a recursão e chama a euristica do tabuleiro com o jogador atual pra resolver

    if jogador == eu:                                           #Max
        melhor = -float('inf')                                  #percorreremo todas as possiblidades a partir do tabuleiro atual e retornar o valor da maior delas por isso o -infinito
        for jogada in jogadas:                                  #o laço de repetição vai em jogada por jogada para testar o maior valor
            resultado = resultJogada(tabuleiro, jogada, jogador)    #resultado guarda a jogada feita em resultJogada()
            valor = minimax(resultado, 'O' if jogador == 'X' else 'X', eu, alpha, beta, maxdepth-1)  #qual o valor do tabuleiro depois de fazer a jogada que está dentro de resultJogada()
            melhor = max(melhor, valor)                         #usando uma função do python para retornar o valor maximizado
            alpha = max(alpha, melhor)                          #vamos pegar o maior valor entre alha e melhor
            if beta <= alpha:                                   #se o valor atual for maior do que o a maior até o momento então...
                break                                           #aqui a gente podou valores menores valores das outros galhos da arvore que são subsequente
        return melhor                                           #se não houver a poda, retorna a maxima
    else:                                                       #Min
        melhor = float('inf')                                   #agora faremo o contrário, pegamos o infinito positivo e verificamos os menores valores possiveis para substituir
        for jogada in jogadas:                                  #o laço para ver todas as jogadas
            resultado = resultJogada(tabuleiro, jogada, jogador)       #resultado verifica a jogada
            valor = minimax(resultado, 'O' if jogador == 'X' else 'X', eu, alpha, beta, maxdepth-1)  #valor pega o resultado da jogada anterior e passa ela pro minimax
            melhor = min(melhor, valor)                                         #a melhor agora recebe o valor minimo
            beta = min(beta, melhor)                                          #o beta agora vai receber o valor minimo entre o valor atual e a melhor jogada
            if beta <= alpha:                                               #se o valor que passou pelo minimax for menor que o atual então...
                break                                                       #vamos podar os valores menores aqui durante a minima tbm    
        return melhor                                                         #se não haver poda, a gente retorna a minima
        
def melhorAcao(tabuleiro, eu):                      #retorna a melhor jogada
    jogadas = jogadasPossiveis(tabuleiro)           #recebe a lista de todas as jogadas possiveis
    melhor = -float('inf')                        #Inicializar o valor infinito negativo, assim, qualquer valor recebido por ele vai ser maior e assim este será substituido
    melhorAc = None                              #inicia a melhor ação sem nenhuma valor
    
    for jogada in jogadas:                      #percorre todas as jogadas possiveis de jogada em jogada
        resultado = resultJogada(tabuleiro, jogada, eu)            #chama a computação de resultados e passa como parametro o tabuleiro, a lista de jogadas possiveis e se o jogador é x ou o
        valor = minimax(resultado, 'O' if eu == 'X' else 'X', eu, -float('inf'), float('inf'), 3)    #valor recebido de 'resultado' passa agora pelo minimax que recebe como parametro onde o X ou O foi jogada e tambem a profundidade d pesquisa, quando chegar a zero ele começa a usar a heuristica, o valores infinitos são para garantir que não estamos valores maiores ou menores que os alhpa e beta.
        if valor > melhor:                        #se valor recebido do minimax é maior que melhor(o que é lógico) então...
            melhor = valor                        #as melhor recebe o minimax
            melhorAc = jogada                    #e a melhor ação recebe a lista na posição atual do laço
    return melhorAc

def jogo():                                     #aqui a gente inicia o jogo de verdade
    tabuleiro = [[None, None, None],                #inicializamos a matriz com nenhum valor
             [None, None, None],
             [None, None, None]
    ]

    jogadorAtual = 'X'                          #vamos inicializar o jogador atual como sendo os desafiantes da IA, e eles começaram com 'X'
    jogando = True                              #vamos criar uma variavel controle do nosso laço, claro que a gente podia usar True no laço...
    vencedor = None                             #vencedor recebe nenhum pois ainda não temos vencedores

    while jogando:                              #inicia o laço do jogo
        desenharTabuleiro(tabuleiro)                #chama a função para desenhar o tabuleiro
        pygame.display.flip()                   

        if jogadorAtual == 'O':                 #a iA joga com 'O', ou seja, se for a vez do 'O' ele chama a IA pra jogar
            time.sleep(1)                       #pra dar um pequeno delay pra jogada da IA
            jogada = melhorAcao(tabuleiro, 'O')     #a jogada da IA é manda para ser analisada
            if jogada is not None:              #garantindo que o algotimo não preencha campos 'cheios' com outra informação
                tabuleiro[jogada[0]][jogada[1]] = 'O'   #marcamos a posição da matriz com 'O'
                vencedor = checarVencedor(tabuleiro)   #vamos checar pra ver se alguém venceu
                if vencedor:                    #se venceu, vamos ver quem
                    print(f'O jogador {vencedor} venceu!')  #se 'X' venceu ou se 'O' venceu
                elif estaCheio(tabuleiro):                         #se estiver cheio, deu velha
                    print(f'Empate')                        #impre o empate
                jogadorAtual = 'X'                          #se não entrarmos em nenhuma desses laços condicionais, o jogador atual vira o X
        else:
            for evento in pygame.event.get():               #vamos garantir que o jogo fechará corretamente dessa vez
                if evento.type == pygame.QUIT:              #em caso de o usuário clicar no X da janela
                    jogando = False                         #o laço jogando para
                    finalizar()                             #para evitar bug na tela de o jogo não fechar imediatamente, chamamos uma função que fechará tudo

                if evento.type == pygame.KEYDOWN:           #o mesmo para apertar ESC
                    if evento.key == pygame.K_ESCAPE:
                        jogando = False
                        finalizar()

                if evento.type == pygame.MOUSEBUTTONDOWN and vencedor is None:      #aqui pegamos em qual retangulo o usuário clicou
                    mouseX, mouseY = pygame.mouse.get_pos()                         #sua posição de X e Y agora são variáveis

                    linha = mouseY // tamanhoQuadrado                               #tentamos pegar a posição clicada e colocála dentro como parametros da nossa matriz
                    coluna = mouseX // tamanhoQuadrado

                    if tabuleiro[linha][coluna] is None:                                #ele vai pegar os parametros da matriz e verificar se ela está vazzia
                        tabuleiro[linha][coluna] = jogadorAtual                         #caso vazia ele vai completar com quem está atualmente jogado, se 'X' senão 'O'

                        vencedor = checarVencedor(tabuleiro)                               #depois de marcado, vamos verificar se alguém já venceu

                        if vencedor:                                                #mesma coisa doq ue tá lá em cima, se venceu, escreve na tela
                            print(f'O jogador {vencedor} venceu!')
                        elif estaCheio(tabuleiro):                                         #se tá cheio, então temos um epate
                            print(f'Empate')

                        jogadorAtual = 'O' if jogadorAtual == 'X' else 'X'          #não pode esquecer de mudar o jogador depois de ver que o jogo ainda não acobou, seja por vitoria o empate que seja

        if vencedor or estaCheio(tabuleiro):                                               #se houver o fim de jogo, vamos escrever isso no meio da tela
            tela.fill((0, 0, 0))
            textoFinal = fonte.render(f'{vencedor} venceu' if vencedor else 'Empate!', True, (255, 255, 255))
            tela.blit(textoFinal, (150, 250))
            pygame.display.flip()
            time.sleep(4)
            Jogando = False
            finalizar()
            
    pygame.quit()
    
jogo()
