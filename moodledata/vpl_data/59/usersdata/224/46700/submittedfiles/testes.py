# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
s=0
for num in range(1,n+1,1):
    if num%2==1:
        s=s+num/(num**2)
    else:
       s=s-num/(num**2)
print(s)