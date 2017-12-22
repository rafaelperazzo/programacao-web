# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
'''
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]')
nome = str(input('Qual seu nome? '))
s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
while s =! X or s =! O:
    print('Isira um símbolo válido')
    s = str(input('Qual símbolo você deseja utilizar no jogo? '))
if s = X

print(sorteio(inicio))
'''
# Jogo da Velha
#

# O tabuleiro
velha="""               Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""
# Uma lista de posições (linha e coluna) para cada posição válida do jogo
# Um elemento extra foi adicionado para facilitar a manipulação
# dos índices e para que estes tenham o mesmo valor da posição
#
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3

posições = [
       None,  # Elemento adicionado para facilitar índices
      (5, 1), # 1
      (5, 5), # 2
      (5, 9), # 3
      (3, 1), # 4
      (3, 5), # 5
      (3, 9), # 6
      (1, 1), # 7
      (1, 5), # 8
      (1, 9), # 9
    ]

# Posições que levam ao ganho do jogo
# Jogadas fazendo uma linha, um coluna ou as diagonais ganham
# Os números representam as posições ganhadoras
ganho = [
          [ 1, 2, 3], # Linhas
          [ 4, 5, 6],
          [ 7, 8, 9],
          [ 7, 4, 1], # Colunas
          [ 8, 5, 2],
          [ 9, 6, 3],
          [ 7, 5, 3], # Diagonais
          [ 1, 5, 9]
        ]
