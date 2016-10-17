# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite o valor de a='))
b=int(input('Digite o valor de b='))
c=int(input('Digite o valor de c='))
d=int(input('Digite o valor de d='))
if a==c and b!=d:
    print('V')
if b==d and a!=c:
    print('v')
else:
    print('F')
