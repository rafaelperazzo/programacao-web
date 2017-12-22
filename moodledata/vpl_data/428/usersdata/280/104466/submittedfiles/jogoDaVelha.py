# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
j = 'X'
for i in range(9):
    print('Faça a primeira jogada')
    p = str(input(''))
    jogada(p,j)
    print(tabuleirob())