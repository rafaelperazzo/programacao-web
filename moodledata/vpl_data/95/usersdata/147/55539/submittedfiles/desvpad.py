# -*- coding: utf-8 -*-
import math

#comece abaixo
listax[]
n=int(input('digite n:'))
for i in range(1,n+1,1):
    valor=float(input('digite valor:'))
    lista.append(valor)
soma=0
for i in range(0,len(listax),1):
    soma=soma+listax[i]
media=soma/len(listax)
print('%.2f' listax[0])
print('%.2f' listax[n-1])
print('%.2f' media)
print(listax)
n=len(listax)
soma2=0
for i in range(0, len(listax),1):
    soma2=soma2+((listax[i]-media)**2)
desvp=(soma2/(n-1))**0.5
print('%.2f' %desvp)