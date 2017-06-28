# -*- coding: utf-8 -*-
import numpy as np

def cortel1(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                l1=i
    return l1
    
def cortel2(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                l2=i
    return l2

def cortec1(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                c1=j
    return c1

def cortec2(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                c2=j
    return c2

n=int(input('Digite o número de linhas:'))
m=int(input('Digite o número de colunas:'))

a=np.zeros((n,m))
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            a[i,j]=int(input('Valor:'))

l1=  
