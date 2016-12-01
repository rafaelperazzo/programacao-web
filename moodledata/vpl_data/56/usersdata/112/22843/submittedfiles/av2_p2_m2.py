# -*- coding: utf-8 -*-
from __future__ import division
a=[]
n=input('Digite a quantidade de salas:')
a.append(input('Digite a quantidade de vidas de cada sala:')
entrada=input('Digite a entrada:')
saida=input('Digite a saida:')

def vidas(entrada,saida):
    for i in range (0,len(a)-1,1):
        soma=0
        for j in range (entrada,saida,1):
            soma=soma+j
    return soma
print vidas(entrada,saida)