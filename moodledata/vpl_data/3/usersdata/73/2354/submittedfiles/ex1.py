# -*- coding: utf-8 -*-
from __future__ import division
a= input ('digite o valor de a:')
b= input ('digite o valor de b:')
c= input ('digite o valor de c:')
d=b*b(-4*a*c)
if d>=0:
    x1=(-b+(b*b(-4*a*c))**0.5)/(2*a)
    print ('x1=%.2f' %x1)
    x2=(-b-(b*b(-4*a*c))**0.5)/(2*a)
    print ('x2=%.2f' %x2)
else:
    print('SRR')
        