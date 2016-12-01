# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import division
import numpy as np

def simetricaC(a,x,y):
    colunaC=a[x,y]
    soma=0
    for i in range(0,a.shape[0],1):
        f=a.shape[0]-1
        for j in range(0,colunaC,1):
            soma=a[i,j]+a[i,f]
            f=f-1
    return soma 


        
n=input('Digite a quantidade de linhas:')
x=3
y=3
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')

final=(-1)**simetricaC(a,x,y)
print(final)
