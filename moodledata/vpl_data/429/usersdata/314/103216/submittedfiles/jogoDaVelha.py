# -*- coding: utf-8 -*-
import random 
from jogoDaVelha_BIB import *

grupo = 'Breendon'
jogador = ''
simboloJogador = ''
simboloPC = ''
 
print('Bem vindo ao JogodaVelha do grupo {} \n' .format(grupo)) 
jogador = input('Qual seu nome (ou apelido)? ')
simboloJogador = solicitaSimboloDoHumano()

if simboloJogador == 'X':
    simboloPC = 'O'
else:
    simboloPC = 'X'

    
