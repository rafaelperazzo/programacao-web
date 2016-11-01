# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite a quantidade de valores: ')

l=[]
soma=0
soma2=0
for i in range(0,n,1):
    l.append(input('Digite um valor: '))
    soma=soma+l[i]
media= soma/n
for i in range(1,n+1,1):
    soma2=((i-media)**2)

s= ((1//(n-1))*soma2)**(1/2)
print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %media)
print ('%.2f'%s)