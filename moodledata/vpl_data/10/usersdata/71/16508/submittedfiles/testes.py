# -*- coding: utf-8 -*-
from __future__ import division

x=[0,1,2,3,4,7,6]

cont=0
for i in range(0,len(x),1):
    if i==0:
        if x[i]>x[i+1]
    elif i==len(x)-1:
        if x[i]>x[i-1]:
            cont=cont+1
    else: 
        if x[i]>x[i+1] and x[i]>x[i-1]:
            cont=cont+1
if cont==1:
    print "S"
else:
    print "N"
    
    