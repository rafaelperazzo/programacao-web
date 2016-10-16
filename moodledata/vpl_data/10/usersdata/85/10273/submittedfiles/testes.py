# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite o valor de n: '))

f=1
s=1
for i in range(1,n+1,1):
    f=f*i
    a=1/f
    s=s+a
print s