# -*- coding: utf-8 -*-
from __future__ import division
import math
#1
a = input('Digite o valor de a :')
b = input('Digite o valor de b :')
c = input('Digite o valor de c :')
d = input('Digite o valor de d :')

#2 

if a>b>c>d:
    print('S')
if a<b>c>d:
    print('S')
if a<b<c>d:
    print('S')
if a<b<c<d:
    print('S')
else:
    print('N')
    