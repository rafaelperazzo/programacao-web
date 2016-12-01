# -*- coding: utf-8 -*-
from __future__ import division
a=[]
n=input('Digite a quantidade de salas:')
for i in range(0,n,1):
    a.append(input('Digite o valor de cada sala:'))
ent=input('Digite a sala de entrada:')
sai=input('Digite a sala de saida:')
def vidas(entrada,saida):
    soma=0
    for j in range (entrada+1,saida,1):
        soma=soma+j
    return soma
print vidas(ent,sai)