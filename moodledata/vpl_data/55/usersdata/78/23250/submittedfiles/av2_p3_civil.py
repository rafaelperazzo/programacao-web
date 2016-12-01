# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 

def soamalinhas(a,x):
    
    
n=input('digite a dimensão da matriz:')
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento da matriz:')
    
