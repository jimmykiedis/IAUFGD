TicTacToeAB - Jogo da Velha com IA (Minimax + Pygame)

=====================================================

🎮 DESCRIÇÃO DO PROJETO
------------------------
Este projeto implementa o clássico Jogo da Velha com interface gráfica usando a biblioteca pygame
e uma inteligência artificial que decide jogadas com base no algoritmo Minimax com poda Alpha-Beta.

A IA avalia jogadas futuras usando uma função heurística que considera oportunidades e ameaças
no tabuleiro, buscando maximizar suas chances de vitória e minimizar as do oponente.

Ideal para fins acadêmicos, estudos sobre IA em jogos, e diversão com Python!


🧠 FUNCIONALIDADES
-------------------
- Jogador humano vs IA
- Interface gráfica com cliques do mouse
- Detecção de vitória ou empate
- IA estrategista usando heurística
- Algoritmo Minimax com poda Alpha-Beta


🛠️ TECNOLOGIAS USADAS
-----------------------
- Python 3.x
- Pygame
- Lógica de IA com Minimax e heurística simples


🚀 COMO EXECUTAR
-----------------
1. Instale o Python 3 (se ainda não tiver)
2. Instale a biblioteca pygame:
   pip install pygame

3. Execute o arquivo principal:
   python nome_do_arquivo.py

*Substitua "nome_do_arquivo.py" pelo nome correto do seu script (ex: tictactoe.py)*


📂 ESTRUTURA DO CÓDIGO
-----------------------
- desenharTabuleiro()   → Desenha o grid e as peças (X/O)
- checarVencedor()      → Verifica se há ganhador
- heuristica()          → Avalia o estado do tabuleiro
- minimax()             → Aplica IA com recursão e poda
- melhorAcao()          → IA escolhe a melhor jogada
- jogo()                → Loop principal do jogo


🧩 OBSERVAÇÕES
---------------
- IA joga com 'O' e sempre começa após o humano ('X')
- A profundidade da IA está limitada a 3 para manter desempenho
- Use ESC ou o botão de fechar para sair do jogo


📈 MELHORIAS FUTURAS
---------------------
- Adicionar placar de vitórias
- Seleção de dificuldade
- Modo "IA vs IA"
- Botão de reiniciar partida


👨‍💻 AUTORIA
-------------
Desenvolvido por: [Seu Nome ou Apelido Aqui]
Projeto educacional para estudos em Ciência da Computação

