def cabecalho():"""
|=================================================================|
|          BEM VINDO AO JOGO DA VELHA DO GRUPO G                  |
|                                                                 |
|      (Aquila, Joao Otavio, Jose Salviano, Werick)               |
|=================================================================|
"""

velha():"""
00|01|02
10|11|12
20|21|22
"""

posicoes_na_matriz = [
    (0,0),
    (0,1),
    (0,2),
    (1,0),
    (1,1),
    (1,2),
    (2,0),
    (2,1),
    (2,2),
    ]
vencedor = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 3],
    ]
velha = []
for linha in cabecalho():
    velha.append(list(linha))

jogador = "X" # Começa jogando com X
jogando = True
jogadas = 0 # Contador de jogadas - usado para saber se velhou
while True:
    for t in velha:  # Imprime o tabuleiro
        print("".join(t))
    if not jogando: # Termina após imprimir o último tabuleiro
        break
    if jogadas == 9: # Se 9 jogadas foram feitas, todas as posições já foram preenchidas
        print("Deu velha! Ninguém ganhou.")
        break
    jogada = int(input("Digite a posição a jogar 1-9 (jogador %s):" % jogador))
    if jogada<1 or jogada>9:
        print("Posição inválida")
        continue
    # Verifica se a posição está livre
    if velha[posicoes_na_matriz[jogada][0]][posicoes_na_matriz[jogada][1]] != " ":
        print("Posição ocupada.");
        continue
    # Marca a jogada para o jogador
    velha[posicoes_na_matriz[jogada][0]][posicoes_na_matriz[jogada][1]] = jogador
    # Verfica se ganhou
    for p in vencedor:
        for x in p:
            if velha[posicoes_na_matriz[x][0]][posicoes_na_matriz[x][1]] != jogador:
                break
        else: # Se o for terminar sem break, todas as posicoes de p pertencem ao mesmo jogador
            print("O jogador %s ganhou (%s): "%(jogador, p))
            jogando = False
            break
    jogador = "X" if jogador == "O" else "O" # Alterna jogador
    jogadas +=1 # Contador de jogadas

# Sobre a conversão de coordenadas:
# tabuleiro[posições[x][0]][posições[x][1]]
#
# Como tabuleiro é uma lista de listas, podemos acessar cada caracter
# especificando uma linha e uma coluna. Para obter a linha e a coluna, com base
# na posição jogada, usamos a lista de posições que retorna uma tupla com 2 elementos:
# linha e coluna. Sen
