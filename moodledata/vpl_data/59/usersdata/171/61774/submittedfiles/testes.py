# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
import numpy as np
def media(a):
    m=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        media=soma/(a.shape[1])
        m.append(media)
    return(m)
n=int(input('digite n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('digite numero:'))
print(media(a))
    