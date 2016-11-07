# -*- coding: utf-8 -*-
from __future__ import division

a=[0,1,2,3,4,7,6]
cont=0

for i in range(1,len(a)-2,1):
    if a[i-1]>a[i] and a[i]>a[i+1]:
        cont=cont+1
if a[0]>a[i]:
    cont=cont+1
if a[len(a)-1]>a[len(a)-2]:
    cont=cont+1
        
print cont