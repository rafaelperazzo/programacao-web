# -*- coding: utf-8 -*-
from __future__ import division
def soma(n,p,s):
    a=[]
    soma=0
    for i in range (p,s+1,1):
        soma=soma+a[i]
    
    return soma
def maiorSoma(z):
    z=z[0]
    for i in range (0,len(z),1):
        if (a<z[i]):
            z=z[i]
    return a

n=input('Digite a quantidade se salas:')

p=input('Digite a porta de entrada:')
s=input('Digite a porta de saída:')
b=[]
for i in range (0,n,1):
    b.append(input('digite o elemento da lista:'))
c=soma(n,p,s)
d=maiorSoma(s)
print(d)


