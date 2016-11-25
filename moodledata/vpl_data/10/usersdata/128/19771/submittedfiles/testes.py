# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

import numpy as np

def linhaAcima(a):
    for j in range (0,a.shape[1]+1,1):
        for i in range (0,a.shape[0]+1,1):
            if a[i,j]==1:
            return i
            break
        
    