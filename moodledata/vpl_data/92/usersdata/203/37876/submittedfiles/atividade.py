# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
num=1
den=n
S=0
for i in range(1,n+1,1):
    S=S+(num/den)
    num=num+1
    den=den-1
print(S)

    