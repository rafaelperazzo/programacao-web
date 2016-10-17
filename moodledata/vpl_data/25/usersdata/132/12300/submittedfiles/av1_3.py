# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
i=a
c=4
while True:
    if a%i==0 and b%i==0:
        print('MDC %.1f'%i)
        break
    i=i-1
print('numero de divisoes %.1f'%c)    