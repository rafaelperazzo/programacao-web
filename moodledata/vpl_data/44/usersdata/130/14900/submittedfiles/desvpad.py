# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
x=[]
for i in range(0,n,1):
    x.append(input('Digite um elemento:'))
print(x[0])
print(x[len(x)-1])
s=0
for i in range(0,n,1):
    s=s+x[i]
s=s/(len(x)) 
print(s)

