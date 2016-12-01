# -*- coding: utf-8 -*-
from __future__ import division

def vidas(p,e,s):           #p=portas; e=entrada; s=saida.
    x=0
    for i in range(e,s+1,1):
        x=x+p[i]
    return x
    
p=input('Digite a porta de entrada:')
s=input('Digite a porta de saida:')
a=[]
for i in range(0,n,1):
    print('Porta %d' %(i+1))
    a.append(input('TOTAL DE VIDAS:')
print ('A soma das vidas é:%d' %vidas(a,e,s))