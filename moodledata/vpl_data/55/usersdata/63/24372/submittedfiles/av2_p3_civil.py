# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def sl(a,l):
    sl=0
    for j in range (0,a.shape[1],1):
        sl=sl+a[l,j]
    return sl
    
def sc(a,c):
    sc=0
    for i in range (0,a.shape[0],1):
        sc=sc+a[i,c]
    return sc
    
def p(a,x,y):
    st=(sl(a,x)+sc(a,y))-(2*a[x,y])
    return st
    
n=input('Digite n:')

linhas=input('Digite a posição das linhas :')
colunas=input('Digite a posiçã das colunas:')

a = np . zeros ( ( n,n ) )
for i in range (0, a.shape[0],1):
    for j in range (0, a.shape[1],1):
        a[i,j]=input('Digite os elementos:')

peso=p(a,linhas,colunas)
print('%d'%peso)