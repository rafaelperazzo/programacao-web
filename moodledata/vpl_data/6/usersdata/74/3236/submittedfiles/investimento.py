# -*- coding: utf-8 -*-
from __future__ import division

i = input('Digite o valor do investimento:')
tcp = input('Digite a taxa de crescimento percentual em valor decimal')

#Anos seguidos

a1 = i+i*tcp
a2 = a1+a1*tcp
a3 = a2+a2*tcp
a4 = a3+a3*tcp
a5 = a4+a4*tcp
a6 = a5+a5*tcp
a7 = a6+a6*tcp
a8 = a7+a7*tcp
a9 = a8+a8*tcp
a10 = a9+a9*tcp

print('%.2f'% a1)
print('%.2f'% a2)
print('%.2f'% a3)
print('%.2f'% a4)
print('%.2f'% a5)
print('%.2f'% a6)
print('%.2f'% a7)
print('%.2f'% a8)
print('%.2f'% a9)
print('%.2f'% a10)

