# -*- coding: utf-8 -*-
def soma(a):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape1],1):
            if i!=j:
                soma=soma+a[i,j]
        b.append(soma)
    return(b)
def diagonal(a,b):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                if a[i,j]<b[i]:
                    return False
    return True

import numpy as np
n=int(input('digite n:'))
a=np.zeros((n,n))
