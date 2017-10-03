# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
if n<0:
    n=n*(-1)
i=0
s=0
while i<n:
    s=s+(i+1)/(n-i)
    i=i+1
print(.5f %s)

