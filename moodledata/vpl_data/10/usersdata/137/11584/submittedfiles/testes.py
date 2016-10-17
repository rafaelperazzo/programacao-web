# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite n:'))
soma=0
for i in range (0,n+1,1):
    x=int(input('x:'))
    if x%2==0:
        soma=soma+x
    print soma
    