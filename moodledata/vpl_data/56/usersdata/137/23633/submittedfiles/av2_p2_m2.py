# -*- coding: utf-8 -*-
from __future__ import division
def soma(n,p,s):
    a=[]
    soma=0
    for i in range (p,s+1,1):
        soma=soma+a[i]
    a.append(soma)
    return soma
def maiorSoma(s):
    s=s[0]
    for i in range (0,len(s),1):
        if (a<s[i]):
            s=s[i]
    return a

n=input('Digite a quantidade se salas:')

p=input('Digite a porta de entrada:')
s=input('Digite a porta de saída:')
b=[]
for i in range (0,n,1):
    b.append(input('digite o elemento da lista:'))
c=soma(m,p,s)
d=maiorSoma(s)
print(d)


