# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
s=0
i=1
if n<0:
    n=n*-1
for i in range(1,n+1,1):
    soma=i/n
    s=s+soma
    i=i+1
    n=n-1
print(s)