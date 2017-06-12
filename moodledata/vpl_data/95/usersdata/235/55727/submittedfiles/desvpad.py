# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite o numero de elementos da lista:'))
x=[]
for i in range(1,n+1,1):
    y=float(input('digite um elemento:'))
    x.append(y)
soma=0
for i in range(0,n,10):
    soma=soma+x[i]
media=soma/n
s=0
for i in range(0,n,1):
    s=s+((x[i]-media)**2)
dp=(s/(n-1))**(1/2)
print('%.2f'%x[0])
print('%.2f'%x[len(x)-1])
print('%.2f'%media)
print('%.2f'%dp)