# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o valor da primeira carta: ')
b = input('Digite o valor da segunda carta: ')
c = input('Digite o valor da terceira carta: ')
d = input('Digite o valor da quarta carta: ')
e = input('Digite o valor da quarta carta: ')

if a>b>c>d>e:
    print "C"

elif e>d>c>b>a:
    print "D"
    
else:
    print "N"