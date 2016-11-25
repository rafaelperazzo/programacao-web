# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE9 AQUI ABAIXO
import numpy as np
def diag1(a):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,i]
    return s
def diag2(a):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,a.shape[0]-i-1]
    return s
def linha(a,n):
    s=0
    for i in range(0,a.shape[1],1):
        s=s+a[n,i]
    return s
def coluna(a,n):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,n]
    return s
def quadradoMagico(a):
    b=[]
    b.append(diag1(a))
    b.append(diag2(a))
    for i in range(0,a.shape[0],1):
        b.append(linha(a,i))
        b.append(coluna(a,i))
    cont=0
    for i in range(1,len(b),1):
        if b[i]!=b[0]:
            cont=cont+1
    if cont==0:
        return 'SIM'
    else:
        return 'NAO'
a=np.zeros((3,3))
a[0,0]=4
a[0,1]=9
a[0,2]=2
a[1,0]=3
a[1,1]=5
a[1,2]=7
a[2,0]=8
a[2,1]=1
a[2,2]=6
print(quadradoMagico(a))