# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE AQUI ABAIXO
def misterio(x):
    b=[]
    for i in range (0,x.shape[0],1):
        for j in range (0,x.shape[1],1):
            b.append(a[j,i])
    return b
a=np.zeros((4,4))
for i in range (0,a.shape[0],1):
    for i in range (0,a.shape[1],1):
        a[i,j]=input('Digite:')
print misterio(a)
        