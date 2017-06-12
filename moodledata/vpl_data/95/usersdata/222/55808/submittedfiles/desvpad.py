# -*- coding: utf-8 -*-
import math
n=int(input('n:'))
lista=[]
soma=0
for i in range(0,n,1):
    num=float(input('num:'))
    lista.append(num)
print('%.2f' % lista[0])
print('%.2f' % lista[len(lista)-1])
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
print('%.2f' % media)
n=len(lista)
soma2=0
for i in range(0,len(lista),1):
    soma2=soma2+((lista[i]-media)**2)
desvpad=(soma/(n-1))**(0,5)
print('%.2f' % desvpad)

