# -*- coding: utf-8 -*-
from __future__ import division
a = input('valor de a')
b = input('valor de b')
c = input('valor de c')

if a>=b and b>=c:
    print ('%.2f' %a)
elif b>=c and b>=a:
    print ('%.2f' %b)
else:
    print ('%.2f' %c)
    