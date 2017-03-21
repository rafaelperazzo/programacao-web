# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
l=input("digite o numero de linhas: ")
c=input("digite o numero de colunas: ")
a=np.zeros((l,c))
for i in range(0,a.shape[0]):
    for j in range(0,a.shape[1]):
        a[i,j]=input("linha %i coluna %i: "%(i+1,j+1))
print a
def quadrada(matriz):
    if matriz.shape[0]==matriz.shape[1]:
        return True
def nulos(m):
    nulo=0
    for i in range(0,a.shape[0]):
        for j in range(0,a.shape[1]):
           if m[i,j]==0:
               nulo+=1
    return nulo
def somad(m):
    soma=0
    for i in range(0,a.shape[0]):
        for j in range(0,a.shape[1]):
            if i==j:
                soma+=a[i,j]
    return soma
def menor(m):
    menor=m[0,0]
    for i in range(0,a.shape[0]):
        for j in range(0,a.shape[1]):
            if a[i,j]<menor:
                menor=a[i,j]
    return menor
def segmenor(m):
     menor=m[0,0]
     segm=[0,0]
    for i in range(0,m.shape[0]):
        for j in range(0,m.shape[1]):
            if m[i,j]<menor:
                menor=m[i,j]
            if m[i,j]<segm and m[i,j]!=menor:
                segm=m[i,j]
    return segm

if quadrada(a):
    print("quadrada")
else:
    print("n quadra")

print nulos(a)
print somad(a)
print menor(a)
print segmenor(a)