# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o valor de A: ')
b = input('Digite o valor de B: ')
c = input('Digite o valor de C: ')

if a>=b>=c>0:
    print 'N'
elif a**2==b**2+c**2:
    print 'S'

elif a**2>b**2+c**2:
    print 'S'

elif a**2<b**2+c**2:
    print 'S'
else: 
    print 'N'
if a**2==b**2+c**2:
    print 'Re'
elif a**2>b**2+c**2:
    print 'Ob'
else:
    print 'Ac'
if a==b==c: 
    print 'Eq'
elif b==c!=a:
    print 'Is'
else:
    print 'Es'