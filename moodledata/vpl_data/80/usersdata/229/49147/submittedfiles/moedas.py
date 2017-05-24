# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('digite os valores das moedas disponíveis:'))
b=int(input('digite os valores das moedas disponíveis:'))
c=int(input('digite cédula:'))

cont=0
qa=c//a
qb=0
while qa>=0:
    troca=c=qa*a
    if troca%b==0:
        
        qb=troca//b
        cont=cont+1
        break
    else:
        qa=qa-1
    if cont>0:
        print qa
        print qb
    else:
        print ('n')