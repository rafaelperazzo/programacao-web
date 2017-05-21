# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
if n<0:
    n=n*-1
s=0
num=1
den=n
for i in range(1, n+1, 1):
    if i<=n:
        num=i+1
    elif n>i:
        den=n-1
    s=s+(num/den)
    i=i+1
print('%.5f' %s)

