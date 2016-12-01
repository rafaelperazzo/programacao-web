# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def PP(m,x,q):
    c1=0
    c2=0
    for i in range(0,m.shape[1],1):
        c1=c1+m[x,i]
    for i in range(0,m.shape[1],1):
        c2=c2+m[i,q]
    c=c1+c2-2*m[x,q]
    return c
m=input('Digite o valor de m:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
m=np.zeros((m,m))
for i in range(0,m,1):
    for j in range(0,m,1):
        m[i,j]=input('Digite um elemento:')
cont=PP(m,a,b)
print('%d'%cont)
