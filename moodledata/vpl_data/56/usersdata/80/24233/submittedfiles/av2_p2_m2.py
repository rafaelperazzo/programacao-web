# -*- coding: utf-8 -*-
from __future__ import division

def conta_vidas(n,e,s):           #n=portas; e=entrada; s=saida.
    x=0
    for i in range (e,s+1,1):
        x=x+n[i]
    return x
    
n=input('Digite o numero de salas:')
e=input('Digite a porta de entrada:')
s=input('Digite a porta de saida:')
k=[]
for i in range(0,n,1):
    print('Porta %d' %(i+1))
    k.append(input('TOTAL DE VIDAS:')
print ('A soma das vidas é:%d' %conta_vidas(k,e,s))