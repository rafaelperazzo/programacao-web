# -*- coding: utf-8 -*-
from __future__ import division
import math
n= int(input('Digite o numero:'))
soma=0
i=1
x=0
y=0

while i<=n:
    s=((1+x)/(n-y))
    x=x+1
    y=y+1
    soma=soma+s
    i=i+1
print ('%.5f' %soma)


