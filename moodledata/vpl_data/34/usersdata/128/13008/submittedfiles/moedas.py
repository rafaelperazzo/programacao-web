# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de uma moeda: ')
b=input('Digite o valor de outra moeda: ')
c=input('Digite o valor da cédula: ')

q1a=c//a
q1b=(c%a)//b

if q1a*a+q1b*b==c:
    print q1a
    print q1b

q2b=c//b
q2a=(c%b)//a

if q2a*a+q2b*b==c:
    print q2a
    print q2b