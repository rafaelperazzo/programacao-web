# -*- coding: utf-8 -*-
from __future__ import division
import math
def maiordegrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        degrau= int(math.fabs(a[i]-a[i+1]))
        if degrau>maior:
            maior=degrau
    return maior

n=input('digite o valor de n:')
a = []
for i in range(0,n,1):
    a.append(input('digite um elemento:'))


print maiordegrau(a)
