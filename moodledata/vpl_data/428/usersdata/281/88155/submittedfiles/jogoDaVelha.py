# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao jogo da velha da equipe ...')
nome=str(input('Qual o seu nome (ou apelido)? '))
simb=str(input('Qual simbolo voce quer utilizar X ou O? '))

if simb==X:
    PC=O
elif simb==O:
    PC=X
else:
    simb=str(input('Qual simbolo voce quer utilizar X ou O? '))
    

