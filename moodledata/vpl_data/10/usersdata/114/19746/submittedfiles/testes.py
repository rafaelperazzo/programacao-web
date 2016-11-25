# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

def transposta (a):
    t = np.zeros( (a.shape[1],a.shape[0]) )
    for i in range (0,a.shape[0],1)
        for j in range (0,a.shape[1],1)
             t[i,j] = a[j,i]
    return t


        
