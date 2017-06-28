# -*- coding: utf-8 -*-
import numpy as np
def transporta(a,b):
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
             b[i,j]==a[j,i]
return(transposta)