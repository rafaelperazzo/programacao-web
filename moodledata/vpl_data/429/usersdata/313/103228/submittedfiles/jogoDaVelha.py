# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
velha="""            posiçoes
   |   |          1 | 2 | 3   
---+---+---      ---+---+---
   |   |          4 | 5 | 6
---+---+---      ---+---+---
   |   |          7 | 8 | 9
"""
posiçoes = [
    None,
    (5, 7),
    (5, 5),
    (5, 3),
    (9, 7),
    (9, 5),
    (9, 3),
    (7, 7),
    (7, 5),
    (7, 3),
            ]
ganha = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [3, 5, 7],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
        ]
tabuleiro = []
for linha in velha.splintlines():
    tabuleiro.append(list(linha))
jodador = "X"
jogando = True
jogadas = 0
while True:
    for t in tabuleiro:
        print("".join(t))
    if not jogando:
        break
    if jogadas == 9:
        print (" deu velha")
        break
    jogada = int(input("digite a posiçao de 1-9 (jogador %s):" % jogador))
    if jogada<1 or jogada>9:
        print(" erro de posiçao)
        continue
    if tabuleiro[posiçoes[jogada][0]][posicoes[jogada][1]] != " ":
        print(" esta posiçao ja foi jogada."):
            continue
        tabuleiro[posições[jogada][0]][posições[jogada][1]] = jogador
        for p in ganho:
            for x in p:
                if tabuleiro[posiçoes[x][0]][posiçoes[x][1]] != jogador:
                    break
            else:
                print("O jogador %s ganhou (%s): "%(jogador, p))
                jogando = False
                break
        jogador = "X" if jogador == "O" else "O"
        jogadas +=1
     
