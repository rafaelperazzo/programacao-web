# -*- coding: utf-8 -*-
import math

n=int(input(''))
a=int(input(''))
b=int(input(''))
l=[]
l2=[]
for i in range(1,n+1,1):
    x=a*i
    l+=[x]
for i in range(1,n+1,1):
    y=b*i
    l2+=[y]
l3=sorted(l+l2)
for i in range(1,n+1,1):
    print(l3[i])
