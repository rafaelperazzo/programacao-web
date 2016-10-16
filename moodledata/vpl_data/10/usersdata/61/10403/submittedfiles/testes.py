# -*- coding: utf-8 -*-
from __future__ import division
import math 
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=input('Digite o valor de d: ')
if a>b and a>c and a>d:
    print ('%.2f maior' %a)
elif b>a and b>c and b>d:
    print ('%.2f maior' %b)
elif c>a and c>b and c>d:
    print ('%.2f maior' %c)
else:
    print ('%.2f maior' %d)
if a<b and a<c and a<d:
    print ('%.2f menor' %a)
elif b<a and b<c and b<d:
    print ('%.2f menor' %b)
elif c<a and c<b and c<d:
    print ('%.2f menor' %c)
else:
    print ('%.2f menor' %d)