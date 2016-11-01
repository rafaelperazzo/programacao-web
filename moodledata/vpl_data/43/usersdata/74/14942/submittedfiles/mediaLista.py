# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de numeros: ')

a = []
i = 1
x = n-1

while x>=i:
    a.append(input('Digite o próximo valor: '))
    i = i+1
un = input('Digite o próximo valor: ')
a.append(un)
b = sum(a)
media = b/n

print('%.2f'% a[0])
print('%.2f'% un)
print('%.2f'% media)
print('%.2f'% a)