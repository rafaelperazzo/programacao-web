# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def somap(a):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,i]
    return s    

n=input('digite o valor de n:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento:')
print(somap(a))        