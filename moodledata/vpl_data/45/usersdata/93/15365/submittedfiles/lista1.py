# -*- coding: utf-8 -*-
from __future__ import division
n=input('n')
a=[]
for i in range(0,n,1):
    a.append(input('n'))
somap=0
somai=0
qp=0
qi=0
for i in range(0,n,1):
    if a[i]%0==0:
        somap=somap+a[i]
        qp=qp+1
    else:
        somai=somai+a[i]
        qi=qi+1
    
        
