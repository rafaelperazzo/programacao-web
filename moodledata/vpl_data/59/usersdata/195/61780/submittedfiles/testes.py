# -*- coding: utf-8 -*-
import numpy as np
def transposta(a,b):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==b[i,j]:
return(a)
n=int(input('numero de linhas:'))
m=int(input('numero de colunas:'))
a=np.zeros((n,m))
a[i,j]=int(input('elemento:'))
print(transposta(a,b))