# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
num=1
den=n
S=num/den
for i in range(1,n+1,1):
    num=num+i
    den=den-i
    S=S+(num/den)
print(S)