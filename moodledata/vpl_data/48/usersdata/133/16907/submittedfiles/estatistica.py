# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio(lista, media):
    s = 0
    for i in range(0, len(lista), 1):
        s = s + (lista[i] - media)**2
    d = (s/(n-1))**0.5
    return d
    
n = input('Digite o número de elementos da lista:')
a = []
b = []
for i in range(0, n, 1):
    a.append(input('Digite o elemento de a:'))
    
for i in range(0, n, 1):
    b.append(input('Digite o elemento de b:'))
    
mediaA = media(a)
mediaB = media(b)
dpa = desvio(a, mediaA)
dpb = desvio(b, mediaB)

print(mediaA)
print(dpa)
print(mediaB)
print(dpb)

