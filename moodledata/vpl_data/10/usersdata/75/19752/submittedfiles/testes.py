# -*- coding: utf-8 -*-
from __future__ import division

def transposta(a):
    c=np.zeros((a.shape[0],1))
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            c[j,i]=a[i,j]
            
    return c 
