# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
r1=input('Digite a quantidade de elementos da lista 1')
J=[]
k=[]
for i in range (0,r1,1):
    J.append(input('asklj'))
    soma=0
    soma=soma+J[i]
    med=J/r1
print(med)