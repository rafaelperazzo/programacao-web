# -*- coding: utf-8 -*-
from __future__ import division

p1= input('Digite o peso da criança no lado esquerdo: ')
c1= input('Digite o comprimento do lado esquerdo da balança: ')
p2= input('Digite o peso da criança no lado direito: ')
c2= input('Digite o comprimento do lado direito da balança: ')

if c1*p1>c2*p2:
    print('-1')

elif c1*p1<c2*p2:
    print('1')

else:
    print('0')