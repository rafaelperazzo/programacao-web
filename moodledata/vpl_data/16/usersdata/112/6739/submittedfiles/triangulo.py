# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
if a<(b+c):
    print('S')
if a>0 and b>0 and c>0 and a<(b+c) and (a**2)==(b**2)+(c**2):
    print('Re')
if a>0 and b>0 and c>0 and  a<(b+c) and (a**2)>(b**2)+(c**2):
    print('Ob')
if a>0 and b>0 and c>0 and  a<(b+c) and (a**2)<(b**2)+(c**2):
    print('Ac')
else:
    print('N')
if a<(b+c) and  a==b==c:
    print('Eq')
if a<(b+c) and  b==c!=a:
    print('Is')
if a<(b+c) and  a!=b!=a:
    print('Es')
if a<0 or b<0 or c<0:
    print('N')