# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite o numero de elementos da lista'))
lista[]
soma=0
for i in range(1,n+1,1):
    valor=float(input('digite o valor:'))
    lista.append(valor)
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
for i in range(0,len(lista),1):
    soma=soma+(lista[i]-media)**2
desvio padrao=(soma/(n-1))**0.5
print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1])
print('%.2f'%lista