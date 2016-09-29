# -*- coding: utf-8 -*-
from __future__ import division

p1=input('Valor do peso da criança do lado esquerdo: ')
c1=input('Valor do comprimento do lado esquerdo: ')
p2=input('Valor do peso da criança do lado direito: ')
c2=input('Valor do comprimento do lado direito: ')

if (p1*c1)==(p2*c2):
    print ('0')
if (p1*c1)>(p2*c2):
    print ('-1')
if (p1*c1)<(p2*c2):
    print ('1')