# -*- coding: utf-8 -*-
import numpy as np
def SomaDaLinha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return(soma)    

