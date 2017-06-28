# -*- coding: utf-8 -*-
import numpy as np
n=int(input('ordem: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        e=float(input('elemento: '))
        a[i,j]==e
print(a)
