# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

lista1=[]
lista2=[]
n=input('digite o valor de n:')

for i in range (0,n,1):
    lista1.append(input('digite os elementos da lista:'))

for i in range (0,n,1):
    lista2.append(input('digite os elementos da lista:'))
    
    
media_lista1=media(lista1)
media_lista1=media(lista2)

lista1=[]
soma1=0
for i in range (0,n-1,1):
    soma1=soma1+(lista1[i]-media)**2
Slista1=(soma1/n-1)**0.5

lista2=[]
soma2=0
for i in range (0,n-1,1):
    soma=soma+(lista2[i]-media)**2
Slista2=(soma/n-1)**0.5

print('%.2f' %media_lista1)
print('%.2f' %Slista1)
print('%.2f' %media_lista2)
print('%.2f' %Slista2)
    
    
    
    
    
    
    
    
    
    