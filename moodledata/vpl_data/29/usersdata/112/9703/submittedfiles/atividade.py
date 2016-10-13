# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
a=1
while n:
    if ((n/(10**a)<1)):
        
        print(a)
    a=a+1