# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('digite o valor de n:'))
m=int(input('digite o valor de m:'))

mdc=a
while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
print(mdc)

