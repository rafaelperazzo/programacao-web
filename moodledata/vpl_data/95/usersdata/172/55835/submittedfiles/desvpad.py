# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite n: '))
a=[]
soma=0
for i in range(0,n,1):
    a.append(float(input('Elementos da lista: ')))
    soma=soma+a[i]
b=a[0]
c=a[n-1]
m=soma/n
s=soma-(m*n)
desvio=((1/(n-1))*(s**2))**0.5
print('%.2f'%b)
print('%.2f'%c)
print('%.2f'%m)
print('%.2f'%desvio)