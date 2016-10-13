# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('quantidade de termos:')
S=0
for in range (1,n+1,1):
    S=S+(math.pow(-1,i+1))/i
print('%.5f' %S)
