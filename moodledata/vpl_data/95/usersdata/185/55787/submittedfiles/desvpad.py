# -*- coding: utf-8 -*-
import math

#comece abaixo
lista=[]
n=int(input('digite a quantidade de elementos:'))
for i in range(0,n,1):
    a=float(input('digite um elemento:'))
    lista.append(a)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
soma2=0
for i in range(0,len(lista),1):
    soma2=soma2+((lista[i]-media)**2)
desvpad=(soma2/(n-1))**(0.5)
print('%.2f'%lista[0])
print('%.2f'%lista[n-1])
print('%.2f'%media)
print('%.2f'%desvpad)
print(lista)