def cabecalho():
    print("|=================================================================|")
    print("|                      JOGO DA VELHA                              |")
    print("|=================================================================|")

def velha():
    print("|                         posições                                |")
    print("|                                                                 |")
    print("|                        1 | 2 | 3                                |")
    print("|                       ---+---+---                               |")
    print("|                        4 | 5 | 6                                |")
    print("|                       ---+---+---                               |")
    print("|                        7 | 8 | 9                                |")
                                              
posicoes_na_matriz = [
    (2,36),
    (2,40),
    (2,44),
    (4,36),
    (4,40),
    (4,44),
    (6,36),
    (6,40),
    (6,44),
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
for linha in cabecalho().splitlines():
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
