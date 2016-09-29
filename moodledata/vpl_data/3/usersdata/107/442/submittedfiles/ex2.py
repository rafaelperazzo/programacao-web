# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
if a<0:
    a=(a**2)
    print('%.2f' %a)
else a>=0:
    a=(a**0.5)
    print('%.2f' %a)
    