# -*- coding: utf-8 -*-
from __future__ import division

def vidas(p,e,s):
    x=0
    for i in range(e,s+1,1):
        x=x+p[i]
    return x
    

p=input('Digite a porta de entrada:')
s=input('Digite a porta de saida:')
k=[]

for i in range(0,p,1):
    print('Vidas da Porta %d' %(i+1))
    k.append(input(':'))

print ('A soma das vidas é:%d' %vidas(k,e,s))