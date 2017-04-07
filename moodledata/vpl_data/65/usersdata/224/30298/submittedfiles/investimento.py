# -*- coding: utf-8 -*-
from __future__ import division

a=float(input('O investimento inicial é de: '))
t=float(input('A taxa de crescimento percentual é de: '))
I1=a+(a*t)
print('%.2f'%I1)
I2=I1+(I1*t)

