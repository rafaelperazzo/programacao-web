# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
s=0
for i in range(1,n+1,1):
    if i%2==1:
        s=s+1/i
    else:
        s=i
print(s)
    

    