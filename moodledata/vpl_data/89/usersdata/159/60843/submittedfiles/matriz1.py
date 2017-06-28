# -*- coding: utf-8 -*-
import numpy as np

def cortel1(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                l1=i
                break
    return 
    
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
                break
    return c1

def cortec2(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                c2=j
    return c2

n= input('Digite o número de linhas:')
m= input('Digite o número de colunas:')

a= np.zeros((n,m))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('Valor:')

l1= cortel1(a)
l2= cortel2(a)
c1=cortec1(a)
c2=cortec2(a)

print(a[l1:(l2+1),c1:(c2+1)])