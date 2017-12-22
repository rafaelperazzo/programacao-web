# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
velha="""            posiçães
   |   |          1 | 2 | 3   
---+---+---      ---+---+---
   |   |          4 | 5 | 6
---+---+---      ---+---+---
   |   |          7 | 8 | 9
"""
posicoes = [
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
    jogada = int(input(
     
