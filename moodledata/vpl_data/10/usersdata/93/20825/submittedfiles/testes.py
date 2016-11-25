# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE9 AQUI ABAIXO
import numpy as np
def solução(a,x,b):
    cont=0
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]*x[j]
        if soma!=b[i]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
        