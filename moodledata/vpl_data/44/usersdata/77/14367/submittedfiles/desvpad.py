# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=int(input('Digite o valor da quantidade de termos:'))

l=[]

for i in range(0,n,1):
    l.append(input('Digite o valores:'))
    
som=0
for i in range(0,n,1):
    soma=soma+l[i]
    
media=soma/n
s=((1/(n-1))*(soma(n-media)**2))**1/2.0

print('%.2f' %l[0])
print('%.2f' %l[n-1])
print('%.2f' %media)
print('%.2f' %s)