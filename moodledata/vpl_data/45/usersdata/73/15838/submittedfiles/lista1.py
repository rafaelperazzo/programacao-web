# -*- coding: utf-8 -*-
from __future__ import division
n=input('digite n:')
a=[]
for i in range (0,n,1):
    a.append(input('número:'))
somap=0
somai=0
qp=0
qi=0
for i in range (0,n,1):
    if a[i]%2==0:
        somap=somap+a[i]
        qp=qp+1
    else:
        somai=somai+a[i]
        qi=qi+1
print somai
print somap
print qi
print qp
print a
