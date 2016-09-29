# -*- coding: utf-8 -*-
from __future__ import division

p1= input('Digite o valor de p1: ')
c1= input('Digite o valor de c1: ')
p2= input('Digite o valor de p2: ')
c2= input('Digite o valor de c2: ')

a= (p1)*(c1)
b= (p2)*(c2)

if a==b:
    print('0')
elif a>b:
    print('-1')
else:
    print('1')