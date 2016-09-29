# -*- coding: utf-8 -*-
from __future__ import division

#1
a = input('digite o valor de a = ')
b = input('digite o valor de b = ')
c = input('digite o valor de c = ')

#2
if a>b and a>c :
    print('%.2f' %a)
elif b>c and b>a :
    print('%.2f' %b)
else :
    print('%.2f' %c)