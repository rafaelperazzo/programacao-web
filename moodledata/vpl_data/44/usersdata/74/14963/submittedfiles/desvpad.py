# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n = input('Digite a quantidade de numeros: ')

a = []
i = 0
x = n-1

while x>i:
    a.append(input('Digite o próximo valor: '))
    i = i+1
un = input('Digite o próximo valor: ')
a.append(un)
b = sum(a)
media = b/n
j = 0
w = 0
while x>=j:
    w = w+(a[j]-media)**2
    j = j+1
s = (w/x)**(1/2)

print('%.2f'% a[0])
print('%.2f'% un)
print('%.2f'% media)
print(a)
print('%.2f'% s)