# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

grupo = 'Breendo'
jogador = ''
simbolo = ''
 
print('Bem vindo ao JogodaVelha do grupo {} \n' .format(grupo)) 
jogador = input('Qual seu nome (ou apelido)? ')
while (simbolo != 'O')  or  (simbolo != 'X'):
    simbolo = input('Qual simbolo deseja ultilizar no jogo? ')

