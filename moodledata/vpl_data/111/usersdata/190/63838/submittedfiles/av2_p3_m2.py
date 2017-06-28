# -*- coding: utf-8 -*-
import numpy as np
def
n=int(input('digite n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o valor:'))


