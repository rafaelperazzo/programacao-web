# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import random
from time import sleep
# COLOQUE SEU PROGRAMA A PARTIR DAQUI
matriz = ['00','01','02'],['10','11','12'],['20','21','22']
print('--------Jogo da Velha----------')
print('\n')

tabuleiro()
nome = input('Qual o seu nome ? ')
print("Vamos ver quem vai ser o 'X' e quem vai ser o 'O': ")
sleep(1.5)
jogador = random.choice((0,1))
if jogador == 1:
    vc = 'X'
    pc = 'O'
else:
    pc = 'X'
    vc = 'O'
print ("%s é: '%s' " %(nome,vc))
print ("O Pc é: '%s' " % pc)
print('\n')
print("Vamos ver quem vai iniciar a partida: ")
sleep(1.5)
primeiro = random.choice((0,1))
if primeiro == 1:
    print('%s começa: '%nome)
else:
    print('Pc começa: ')
p = input('')
