# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de uma moeda: ')
b=input('Digite o valor de outra moeda: ')
c=input('Digite o valor da cédula: ')

if c>=a or c>=b:
    if c%a==0:
        qa=c/a
        print qa
    elif (c%a)%b==0:
        qb=(c%a)/b
        print qb
    elif c%b==0:
        qb=c/b
        print qb
    elif (c%b)%a==0:
        qa=(c%b)/a
        print qa
else:
    print ('Não é possível')