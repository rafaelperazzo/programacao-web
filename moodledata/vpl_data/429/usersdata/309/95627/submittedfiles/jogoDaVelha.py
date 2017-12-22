# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
jogo = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (0, 10, 1):
    a= str(input("SElecione uma posição:"))
    if i%2==0:
        jogo[int(a[0])][int(a[2])]='X'
    else:
        jogo[int(a[0])][int(a[2])]='O'
    for i in range (0,3,1):
         print (str (jogo[i][0]) + '|' + str(jogo[i][1]) + '|' + str(jogo[i][2]))
        