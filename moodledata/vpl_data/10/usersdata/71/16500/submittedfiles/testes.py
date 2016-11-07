# -*- coding: utf-8 -*-
from __future__ import division

a=[0,1,2,3,4,5,6]
cont=0

for i in range(0,len(a)-2,1):
    if a[i]>a[i+1]:
        cont=cont+1
if a[len(a)-2]>a[len(a)-1]:
    cont=cont+1
        
print cont