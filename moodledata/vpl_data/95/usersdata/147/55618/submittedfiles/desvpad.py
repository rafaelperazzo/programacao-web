# -*- coding: utf-8 -*-
import math
lista=[]
n=int(input('digite n:'))
for i in range(1,n+1,1):
    valor=float(input('digite valor:'))
    lista.append(valor)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
print('%.2f' lista[0])
print('%.2f' lista[n-1])
print('%.2f' media)
print(lista)
n=len(lista)
soma2=0
for i in range(0, len(lista),1):
    soma2=soma2+((lista[i]-media)**2)
desvp=(soma2/(n-1))**0.5
print('%.2f' %desvp)