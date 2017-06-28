# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
import numpy as
def transposta(a,b):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            b[i,j]=a[j,i]
    return(b)
n=int(input('digite n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=float(input('digite numero:'))
print(transposta(a,b))