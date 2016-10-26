# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de uma moeda: ')
b=input('Digite o valor de outra moeda: ')
c=input('Digite o valor da cédula: ')

qa=c//a
qb=(c%a)//b

if qa*a+qb*b==c:
    print qa
    print qb