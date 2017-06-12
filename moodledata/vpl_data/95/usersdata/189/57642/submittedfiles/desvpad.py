# -*- coding: utf-8 -*-
import math

n=int(input('digite o numero:'))
lista=[]
for i in range(0,n,1):
    numero=int(input('digite um numero:'))
    lista.append(numero)
    
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)

soma=0
for i in range(0,len(lista),1):
    soma1=soma1+(lista[i]-media(lista))**2
desvio=(soma1/(n-1))**0.5

print('%.2f' %lista[0])
print('%.2f' %lista[n-1])
print('%.2f' %media)
print('%.2f' %desvio)

    
    
