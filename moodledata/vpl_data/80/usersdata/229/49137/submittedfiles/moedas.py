# -*- coding: utf-8 -*-
from __future__ import division

t=int(input('digite os valores das moedas disponiveis:'))
v=int(input('digite os valores das moedas disponiveis:'))
d=int(input('digite cedula:'))

cont=0
qt=d//t
qv=0
while qt>=0:
    troca=d=qt*t
    if troca%v==0:
        
        qv=troca//v
        cont=cont+1
        break
    else:
        qt=qt-1
    if cont>0:
        print qt
        print qv
    else:
        print ('n')