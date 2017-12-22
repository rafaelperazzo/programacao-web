# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import random
# COLOQUE SEU PROGRAMA A PARTIR DAQUI
matriz = ['00','01','02'],['10','11','12'],['20','21','22']
print('--------Jogo da Velha----------')
print('\n')

tabuleiro()
print("Vamos ver quem vai ser o 'X' e quem vai ser o 'O': ")
jogador = random.choice((0,1))
if jogador == 1:
    VC = 'X'
    PC = 'O'
else:
    PC = 'X'
    VC = 'O'
print ("Voce é: '%s' " % VC)
print ("O Pc é: '%s' " % PC)
print('\n')
print("Vamos ver quem vai iniciar a partida: ")
primeiro = random.choice((0,1))
if primeiro == 1:
    print('Você começa: ')
else:
    print('Pc começa: ')
p = input('')

