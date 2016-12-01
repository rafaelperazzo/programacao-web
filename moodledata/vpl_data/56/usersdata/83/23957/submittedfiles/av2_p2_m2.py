# -*- coding: utf-8 -*-
from __future__ import division

def vidas(p,e,s):
    a=0
    for i in range(e,s+1,1):
        a=a+p[i]
    return a


p=input('Digite a quantidade de salas percorridas:   ')
e=input('Digite a quantidade de portas de entrada:   ')
s=input('Digite a quantidade de portas de saída:   ')
l=[]

for i in range (0,p,1):
    print ('Porta(s) %d' %(i+1))
    l.append(input('Qual é o numero vidas: '))

print ('O número de vidas obtidas no jogo é: %d' %vidas(l,e,s))

