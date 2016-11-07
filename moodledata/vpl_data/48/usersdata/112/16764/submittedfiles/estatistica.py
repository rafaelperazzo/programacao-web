# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de números da lista')
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
j=[]
for i in range (0,n,1):
    soma1=0
soma1=((j[i]-resultado)**2)+soma1
S=((1/(n-1))*soma1)**(1/2)
print(S)