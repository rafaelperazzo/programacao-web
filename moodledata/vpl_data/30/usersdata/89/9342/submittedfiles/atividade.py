# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada
n=int(input('digite o valor de n :'))
i=1
s=0
#processamento e saida 
if n<0:
    n=n*(-1)

while i<=n:
    s=s+(i)/(n-(i-1))
    i=i+1

print('%.5f'%s)
