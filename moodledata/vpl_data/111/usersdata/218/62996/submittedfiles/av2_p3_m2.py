# -*- coding: utf-8 -*-
import numpy as np 
N=int(input('digite a dimensão da matriz:'))
a=np.zeros( (N,N) )
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o elemento da matriz:'))
def magica (a):
    sl=[]
    sc=[]
    d=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            sl=sl+a[i,j]
            