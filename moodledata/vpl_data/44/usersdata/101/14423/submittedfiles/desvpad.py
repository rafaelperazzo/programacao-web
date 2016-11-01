# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo


n = input('digite a quantidade de numeros: ')
a = []

for i in range (0,n,1):
    a.append(input('Digite um elemento: '))
    
j = 0
b = 0

for i in range (0,n,1):
    b = a[j]+b
    j = j+1
    

c = a[0]
h = a[n-1]
k = b/n

print ('%.2f' %c)
print('%.2f' %h)
print('%.2f' %k)

soma = 0

for i in range (0,n,1):
    soma = ((a[n]-k)**2)+soma
    a=m+1
    
soma = ((soma)*(1/n-1))
soma = soma**(1/2)

print('%.2f' %soma)