# -*- coding: utf-8 -*-
from __future__ import division

a=[0,1,2,3,4,5,6]
cont=0
if a[0]>a[1]:
    cont=cont+1
if a[len(a)-1]<a[len(a)-2]:
    cont=cont+1

for i in range(1,len(a)-2,1):
    if a[i]>a[i+1]:
        cont=cont+1
        
print cont