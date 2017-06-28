# -*- coding: utf-8 -*-
import numpy as np
def media(a):
    m=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        media=soma/a.shape[1]
        m.append(media)
    return(m)
print(media(a))