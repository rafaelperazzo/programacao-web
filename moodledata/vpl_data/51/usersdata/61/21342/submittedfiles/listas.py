# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    c=[]
    for i in range(0,len(a)-1,1):
        b=a[i+1]-a[i]
        if(b<0):
            b=(-1)*b
        c.append(b)
    return c
    
