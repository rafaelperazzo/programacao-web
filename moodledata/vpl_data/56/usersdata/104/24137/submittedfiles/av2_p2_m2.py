# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite o número de salas:')
salas=[]
for i in range(0,n,1):
    salas.append(input('Digite um valor de vidas:'))
e=input('Digite a porta de entrada:')
s=input('Digite a porta de saída:')
vidas=0
lista=salas[e:(s+1)]
print sum(lista)
    
    

