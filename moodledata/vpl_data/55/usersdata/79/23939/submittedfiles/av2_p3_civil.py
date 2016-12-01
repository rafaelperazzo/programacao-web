# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Processo

def smL(a,x) : 
    sm = 0
    for j in range (0, a.shape[1], 1) :
        sm = sm + a[n,j]
    return sm
    

def smC(a,y) :
    for i in range (0, a.shape[0], 1) :
        sm = sm + a[i,y]
    return sm
    

def smT(a,x,y) :
    sm = 0
    sm = smL(a,x) + smC(a,y) - (2*a[x,y])
    return sm
    
    

#Entrada

N = input('Dimensao da matriz : ')
x = input('Coordenada da linha: ')
y = input('Coordenada da coluna: ')

a = np.zeros ((N,N))

for i in range (0,a.shape[0],1) :
    for j in range (0,a.shape[1],1) :
        a[i,j] = input ('Elementro da matriz 'A': ')
        
sm_T = smt(a,x,y)
print('%d' %sm_T)