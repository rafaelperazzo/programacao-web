# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso(a,x,y):
    lv=[]
    lh=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==y:
                lv.append(a[i,j])
            if i==x:
                lh.append(a[i,j])
    p1=0
    p2=0
    for i in range(0,len(lv),1):
        p1=p1+lv[i]
    for i in range(0,len(lh),1):
        p2=p2+lh[i]
    
    p1=p1-a[x,y]
    p2=p2-a[x,y]
    pt=p1+p2
    return pt
    
n= input('Digite o número de linhas colunas: ')
x= input('Digite
