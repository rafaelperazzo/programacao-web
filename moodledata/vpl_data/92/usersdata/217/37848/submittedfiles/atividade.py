# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
if n<0:
    n=n*-1
i=1
for n in range(1,n-1,1):
    s=i/n
    n=n-1
    i=i+1
print(s)


