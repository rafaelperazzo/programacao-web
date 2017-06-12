# -*- coding: utf-8 -*-
import math

#comece abaixo
lista=[]
n=int(input('digite n:'))
for i in range (0,n,1):
    a=float(input('digite cada elemento:'))
    lista.append(a)
soma=0
for i in range(0,len(lista),1):
    soma=soma+(lista[i])
media=soma/n
soma1=0
for i in range(0,len(lista),1):
    soma1=soma1+(((lista[i])-media)**2)
DP=(soma1/n-1)**(0.5)
print('%.2f'%lista[0])
print('%.2f'%lista[n-1])
print('%.2f'%media)
print('%.2f'%DP)