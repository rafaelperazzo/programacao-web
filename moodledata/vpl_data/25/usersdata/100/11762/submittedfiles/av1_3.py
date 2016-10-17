# -*- coding: utf-8 -*-
from __future__ import division
import math
resultado=0
n=input('n:')
for i in range(0,n,1):
    resultado=resultado+((-1)**i)/(2*i+1)
print resultado
