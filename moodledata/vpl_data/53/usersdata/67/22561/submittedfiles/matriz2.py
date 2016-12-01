# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinha (a):
    sl=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            sl=a[i,j]+sl
    return sl
    
def somacoluna (a):
    sc=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            sc=a[i,j]+sc
    return sc

        




linhas=input("Digite a quantidade de linhas:")
colunas=input("Digite a quantidade de colunas:")
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input("Digite um elemento para a:")
        

slt=0   
for i in range(0,a.shape[0],1):
    slt=a[i,0]+slt
    print slt
print slt
print a