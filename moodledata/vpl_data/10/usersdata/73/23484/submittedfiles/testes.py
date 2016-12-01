# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('n:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('um elemento:')

def centroColuna (a):
    return (a.shape[1]//2
        