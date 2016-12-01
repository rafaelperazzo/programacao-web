# -*- coding: utf-8 -*-
from __future__ import division

def vidas(n,e,s):
    x=0
    for i in range (e,s+1,1):
        x=x+n[i]
    return x
n=int(input('Digite o numero de salas:'))
e=int(input('Digite a porta de entrada:'))
s=int(input('Digite a porta de saida:'))
k=[]
for i in range(0,n,1):
    print('Porta %d' %(i+1))
    a.append(input('TOTAL DE VIDAS:')
print ('A soma das vidas é:%d' %vidas(k,e,s))