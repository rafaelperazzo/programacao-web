# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviop(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio=somatorio+((lista[i]-media)**2)
    resultado=(somatorio/(n-1))**0.5
    return resultado
na=[]
na=input('digite a quantidade:')
for i in range (0,na,1):
    na.append(input('digite um elemento:'))
    
nb=[]
nb=input('digite a qauntidade:')
for i in range (0,nb,1):
    nb.append(input('digite um elemento:'))

media_a = media(a)
desviop_a = desviop(a)
media_b = media(b)
desviop_b = desviop(b)
print media_a
print desviop_a
print media_b
print desviop_b