# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

#ESCREVA UMA FUNÇÃO QUE CALCULA A TRANSPOSTA DE UMA MATRIZ

def transposta(a):
    b = np.zeros( (a.shape[1],a.shape[0]) )
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
            b[i,j] = a[j,i]
    return b

    