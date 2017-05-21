# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
if (n<0):
    n=n*(-1)
i=1
s=0
while (i<=n):
    d=i/n
    i=i+1
    n=n-1
    s=s+d
print(s)    
    

