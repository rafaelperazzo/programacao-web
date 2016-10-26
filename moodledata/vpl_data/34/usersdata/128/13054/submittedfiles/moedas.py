# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de uma moeda: ')
b=input('Digite o valor de outra moeda: ')
c=input('Digite o valor da cédula: ')

if c%a==0:
    print c/a
    print ('0')
elif c%b==0:
    print ('0')
    print c/b
