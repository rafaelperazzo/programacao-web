# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite n: '))
a=[]
soma=0
for i in range(0,n,1):
    a.append(float(input('Elementos da lista: ')))
    soma=soma+a[i]
m=soma/n
soma2=0
for i in range(0,n,1):
    soma2=soma2+((a[i]-m)**2)
b=a[0]
c=a[n-1]
d=((soma2/(n-1))**0.5)
print('%.2f'%b)
print('%.2f'%c)
print('%.2f'%m)
print('%.2f'%d)