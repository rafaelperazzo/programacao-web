# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
s=0
for i in range(1,n+1,1):
    if i%2==0:
        i=i*(-1)
    s=s+(i/(i*i))
print('%.5f'%s)


