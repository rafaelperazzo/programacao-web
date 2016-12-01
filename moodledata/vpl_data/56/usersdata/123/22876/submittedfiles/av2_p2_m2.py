# -*- coding: utf-8 -*-
from __future__ import division

def vidas(f,d,c):
    soma=0
    for i in range(d,c+1,1):
        soma=soma+f[i]
    return soma

l=input('Insira a quantidade de salas:')
f=[]
for i in range(0,l,1):
    f.append(input('Insira uma quantidade de vidas:'))
d=input('Insira o índice da porta de entrada:')
c=input('Insira o índice da porta de saída:')

if d==c:
    print(f[d])
else:
    if c>d:
        print (vidas(f,d,c))
    elif d>c:
        print (vidas(f,c,d))
