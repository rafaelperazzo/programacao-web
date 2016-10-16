# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('n:')
cont=0
p=0
k=0
for i in range (0,n,1):
    f=input('f:')
    if p<f:
        p=f
        cont=cont+1
    if k<cont:
        k=cont
    else:
        p=f
        cont=1
print(k)
