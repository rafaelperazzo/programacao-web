# -*- coding: utf-8 -*-
from __future__ import division

def jogo(a,e,s):
    soma=0
    if s>=e:
        for i in range(e,s+1,1):
            soma=soma+a[i]
    if e>s:
        for i in range(e,s-1,-1):
            soma=soma+a[i]
    return soma
    
n= input('Digite a quantidade de salas: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite a quantidade de vidas da sala: '))

e= input('Digite a entrada: ')
s= input('Digite a saída: ')
    
print jogo(a,e,s)