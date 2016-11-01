# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite a: ')
b=input('Digite b: ')
c=input('Digite c: ')

qa=c//a
qb=(c-qa*a)//b

if c==(a*qa+b*qb):
    print qa
    print qb
    
else:
    print('N')