# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('Digite a ordem da matriz:')
m=np.zeros((n,n))

for i in range(0,m.shape[0],1):
    for j in range(0,m.shape[1],1):
        m[i,j]=input('Digite um elemento:')
    
