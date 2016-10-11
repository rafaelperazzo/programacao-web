# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite n: ')
i=1
soma=0
while n>=1:
    soma=soma+ i/n
    i=i+1
    n=n-1
print('%.5f '%soma)
