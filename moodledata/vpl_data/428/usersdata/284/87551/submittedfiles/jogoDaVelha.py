# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
def jogadaHumana(tabuleiro):
    movimento = 0,0
    for x in range (0,3):
        for y in range (0,3):
            print('%d %d ' % (x,y))
    while movimento not in '1 2 3 4 5 6 7 8 9'.split() or not vazio(tabuleiro, int(movimento)):
        print('Qual a sua jogada, {}?'.format(nome))
        movimento = input()
    return int(movimento)