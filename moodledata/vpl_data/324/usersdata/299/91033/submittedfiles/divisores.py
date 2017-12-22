# -*- coding: utf-8 -*-
import math
l=[1]
l2=[2]
n=int(input(''))
a=int(input(''))
b=int(input(''))
for i in range(1,n+1,1):
    x=a*i
    l+=[x]
for i in range(1,n+1,1):
    y=b*i
    l2+=[y]
for i in range(1,n+2,1):
    print(l[i])

