# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def retangulo(a):
    l1=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                l1=i
                break
    l2=0
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                l2=i
                break
    c1=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                c1=j
                break
    c2=0
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                c2=i
                break
    return (l1,l2,c1,c2)
a=np.zeros((5,5))
a[0,4]=1
a[4,2]=1
print retangulo(a)