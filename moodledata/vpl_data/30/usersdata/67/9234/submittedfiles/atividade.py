# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input("Digite o valor de n:"))
if n<0:
    n=n*(-1)
i=1
j=0
somatorio=0
while (i<=n):
    somatorio=i/(n-j)
    i=i+1
    j=j-1
print("%5.f" %somatorio)
    
    