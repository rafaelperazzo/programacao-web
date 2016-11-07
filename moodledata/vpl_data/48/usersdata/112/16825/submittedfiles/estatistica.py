# -*- coding: utf-8 -*-
from __future__ import division
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def desviopadrao(lista, resultado):
    for i in range (0,n,1):
        soma1=0
        soma1=((j[i]-resultado)**2)+soma1
        S=((1/(n-1))*soma1)**(1/2)
        return S

n = input('Digite o total de elementos de cada lista:')
a=[]
b=[]
for i in range(0, n, 1):
    a.append(input('Digite o elemento:'))
for i in range(0, n, 1):
    b.append(input('Digite o elemento:'))

mediaA = media(a)
mediaB = media(b)
dpa = desviopadrao(a, mediaA)
dpb = desviopadrao(b, mediaB)

print(mediaA)
print(dpa)
print(mediaB)
print(dpb)