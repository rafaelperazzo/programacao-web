# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o valor de a:')
b = input('Digite o valor de b:')
c = input('Digite o valor de c:')
d = input('Digite o valor de d:')

if a==b and a==c and a==d:
    print ('N')
if a>b>=c>=d :
    print ('S')
if d>c>=b>=a:
    print ('S')
if a<b>c>=d:
    print ('S')
if a<=b<c>d:
    print ('S')
else:
    print ('N')