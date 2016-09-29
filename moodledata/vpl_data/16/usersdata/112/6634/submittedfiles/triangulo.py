# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')

if a<b+c and (a**2)==(b**2)+(c**2):
    print('Re')
if a<b+c and (a**2)>(b**2)+(c**2):
    print('Ob')
if a<b+c and (a**2)<(b**2)+(c**2):
    print('Ac')
if a<0 or b<0 or c<0:
    print('N')
    