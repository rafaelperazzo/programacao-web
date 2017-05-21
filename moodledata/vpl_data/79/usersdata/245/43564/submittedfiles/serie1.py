# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n:'))
s=0
for x in range(1,n+1,1):
    if x%2==0:
        s=s-(x/x*x)
    else:
        s=s+(x/x*x)
print(s)
