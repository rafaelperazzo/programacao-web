# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de numeros: ')

a = []
i = 0
x = n-1

while x>=i:
    a.append(input('Digite o próximo valor: '))
    i = i+1
b = sum(a)
media = b/n

print('%.2f'% a[0])
print('%.2f'% a[n])
print('%2f'% media)
print('%.2f'% a)