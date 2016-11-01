# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite a quantidade de vezes:')
a=[]
i=0
soma=0

while i<n:
    a.append(input('Digite um elemento:'))
    i=i+1

i=0
while i<n:
    soma= a[i] + soma
    i=i+1
media=soma/n

somad=0
i=0
while i<n:
    somad= somad+(((a[i])-media)**2)
    i=i+1

s=((((1)/(n-1))*somad)**(1/2))




print('%.2f' %a[0])
print('%.2f' %a[n-1])
print('%.2f' %media)  
print('%.2f' %s)

