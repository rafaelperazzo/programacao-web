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

print('%.2f' %a[0])
print('%.2f' %a[n-1])
print('%.2f' %media)    
print(a)
