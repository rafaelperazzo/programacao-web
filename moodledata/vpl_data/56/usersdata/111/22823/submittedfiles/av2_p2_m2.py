# -*- coding: utf-8 -*-
from __future__ import division

def vidas(lista,a,b):
    soma=0
    for i in range(a,b+1,1):
        soma=soma+lista[i-1]
    return soma
    
n=input('Digite a quantidade de salas: ')
lista=[]
for i in range(0,n,1):
    lista.append(input('Digite o número de vidas da sala: ')

#a=input('Digite a porta de entrada da sala: ')
b=input('Digite a porta de saída da sala: ')

c=vidas(lista,a,b)

print c