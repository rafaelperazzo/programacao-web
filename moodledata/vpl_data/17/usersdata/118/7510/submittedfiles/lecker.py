# -*- coding: utf-8 -*-
from __future__ import division
import math
#1
a = input('Digite o valor de a :')
b = input('Digite o valor de b :')
c = input('Digite o valor de c :')
d = input('Digite o valor de d :')

#2 

if a>b and b<c>d:
    print('N')
elif a<b>c and c<d:
    print('N')
elif a>b and c<d:
    print('N')
elif a<b>c and c<d:
    print('N')
else:
    print('S')
    