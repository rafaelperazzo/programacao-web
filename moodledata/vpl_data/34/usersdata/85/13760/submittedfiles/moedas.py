# -*- coding: utf-8 -*-
from __future__ import division

a= int(input('Digite o valor de a: '))
b= int(input('Digite o valor de b: '))
c= int(input('Digite o valor de c: '))

qa= c//a
qb= (c%a)//b
if ((c%a)%b==0):
    print qa
    print qb
else:
    print('N')
print('Outra saída')
qb= c//b
qa= (c%b)//a
if (c%b)%a==0:
    print qa
    print qb
else:
    print('N')