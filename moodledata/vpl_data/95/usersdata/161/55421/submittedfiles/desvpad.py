# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Informe o número de elementos da lista:'))
lista=[]
soma=0
soma1=0
for i in range(0,n,1):
    numero=int(input('Informe um número:'))
    lista.append(numero)
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
for i in range(0,len(lista),1):
    soma1=soma1+((lista[i]-media(lista))**2)
desvio_padrao=(soma1/n-1)**0.5
print('%.2f' %lista[0])
print('%.2f' %lista[len(lista)-1])
print('%.2f' %media)
print('%.2f' %desvio_padrao)
print(lista)