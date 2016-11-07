# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

a=[]
b=[]
n=input('digite a quantidade de elementos:')
for i in range(0,n,1):
    a.append(input('digite o elemento:'))

for i in range(0,n,1):
    b.append(input('digite o elemento:'))
    
media_a=media(a)
media_b=media(b)

def desvio(lista):
    soma=0
    for j in range (0,len(lista),1):
        soma=((soma+(lista[j]-media(lista)))**2)
        s=((1/(len(lista)-1))**soma)**0.5
        return s
        
desvio_a=desvio(a)
desvio_b=desvio(b)

print('%.2f'%media_a)
print('%.2f'%desvio_a)
print('%.2f'%media_b)
print('%.2f'%desvio_b)

