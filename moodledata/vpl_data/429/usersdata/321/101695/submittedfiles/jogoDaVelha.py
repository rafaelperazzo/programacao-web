# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')
nome = str(input('Qual seu nome? \n'))
simbolo()

j1 = nome
j2 = 'pc'

sort = random.randint(1,2)

if sort == 1:
    print ('Parabéns',j1,'Você Ganhou!!')
else:
    print ('Parabéns',j2,'Você Ganhou!!')
