# -*- coding: utf-8 -*-
import numpy as np

def cortel1(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
                
def cortel2(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                l2=i
    return l2
    
def cortec1(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                c2=j
    return c2
linhas=int(input('linhas:'))
colunas=int(input('colunas:'))

a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('valor:'))
l1=cortel1(a)
l2=cortel2(a)
c1=cortec1(a)
c2=cortec2(a)
print(a[l1:l2+1,c1:c2+a])


