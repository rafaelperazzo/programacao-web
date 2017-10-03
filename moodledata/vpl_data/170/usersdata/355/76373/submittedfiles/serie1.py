# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))

termo=1
m=1
d=m*m
s=0

for termo in range(1,n+1,1):
    if termo%2==0:
        s=s-(m*2-1/d)
    else:
        s=s+(m*2-1/d)
    m=m+1

print('%.5f'%s)



