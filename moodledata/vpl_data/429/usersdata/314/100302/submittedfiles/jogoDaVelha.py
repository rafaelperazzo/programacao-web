# -*- coding: utf-8 -*-
import random 
from jogoDaVelha_BIB import *

grupo = 'Breendon'
jogador = ''
simboloJogador = solicitaSimboloDoHumano()
simboloPC = ''
 
print('Bem vindo ao JogodaVelha do grupo {} \n' .format(grupo)) 
jogador = input('Qual seu nome (ou apelido)? ')
while (simboloJogador != 'O')  and  (simboloJogador != 'X'):
    simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ')

if simboloJogador == 'X':
    simboloPC = 'O'
else:
    simboloPC = 'X'

    
