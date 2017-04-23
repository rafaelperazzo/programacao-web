# -*- coding: utf-8 -*-
import math
n=int(input("digiteo valor de n:"))
s=0
for i in range (1,n+1,1):
    if  (n < 0):
        n=n*(-1)
        s=s+(i)/(n+1-i)
    else:
        n=n
        s=s+(i)/(n+1-i)
print(s)

