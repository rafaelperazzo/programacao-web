# -*- coding: utf-8 -*-
from __future__ import division
def maiorSoma(n,p,s):
    soma=0
    for i in range (p,s+1,1):
        soma=soma+n[i]
    return soma

n=input('Digite a quantidade se salas:')
p=input('Digite a porta de entrada:')
s=input('Digite a porta de saída:')
b=[]
for i in range (0,n,1):
    b.append(input('digite o elemento da lista:'))
c=maiorSoma(b,p,s)
print('%d' %c)


