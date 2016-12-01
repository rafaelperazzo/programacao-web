# -*- coding: utf-8 -*-
from __future__ import division
s=input('Digite a quantidade de salas:')
a=[]
for i in range (0,s,1):
    a.append(input('Digite a quantidade de vidas para a sala:'))
e=input('Informe o índice da sala de entrada:')
s=input('Informe o índice da sala de saída:')
Vidas=0
for i in range (e,s+1,1):
    Vidas=Vidas+i
print Vidas