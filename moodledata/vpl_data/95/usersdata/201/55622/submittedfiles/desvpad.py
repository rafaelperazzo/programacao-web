# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Digite n:'))
lista=[]
for i in range(1,n+1,1):
    valor=float(input('Digite o valor:'))
    lista.append(valor)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
print('%.2f' %lista[0])
print('%.2f' %lista[n-1])
print('%.2f' %media)