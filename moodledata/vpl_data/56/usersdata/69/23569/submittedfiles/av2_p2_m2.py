# -*- coding: utf-8 -*-
from __future__ import division
def vidas(x,e,s):
    soma=0
    for i in range(e,s+1,1):
        soma=soma+x[i]
    return soma
n=input('Digite a quantidade de portas:')
v=[]
for i in range(0,n,1):
    v.append(input('digite a quantidade de vidas de cada sala:'))
e=input ('Digite o número da porta de entrada:')
s=input('digite o número da porta de saída:')
print vidas(v,e,s)
