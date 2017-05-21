# -*- coding: utf-8 -*-
import math
n=int(input('digite n termos:'))
s=0
num=1
for i in range(1,n+1,1):
    if i%2==0:
        s=s-(num/(num**2))
    else:
        s=s+(num/(num**2))
    num=num+1
print('%.5f'%s)

