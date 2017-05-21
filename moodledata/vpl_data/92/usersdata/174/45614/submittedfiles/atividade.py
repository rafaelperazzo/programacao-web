# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
if n<0:
    n=n*-1
s=0
i=0
num=1
den=n
while i<=n:
    s=s+(num/den)
    if i<=n:
        num=i+1
    elif n>i:
        den=n-1
print('%.5f' %s)

