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
        somatorio=somatorio+(lista[i]-media(lista))**2
    resultado=(somatorio/(len(lista)-1))**0.5
    return resultado
a=[]
b=[]
n=input('digite a quantidade:')
for i in range (0,n,1):
    a.append(input('digite um elemento:'))
    

for i in range (0,n,1):
    b.append(input('digite um elemento:'))

media_a = media(a)
desviop_a = desviop(a)
media_b = media(b)
desviop_b = desviop(b)
print ('%.2f'%media_a)
print ('%.2f'%desviop_a)
print ('%.2f'%media_b)
print ('%.2f'%desviop_b)