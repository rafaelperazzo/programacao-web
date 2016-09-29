# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o valor de A: ')
b = input('Digite o valor de B: ')
c = input('Digite o valor de C: ')
d = input('Digite o valor de D: ')

if a>b>c>d or a<b>c>d or a<b<c<d or a<b<c>d:
    print 'S'
else: 
    print 'N'