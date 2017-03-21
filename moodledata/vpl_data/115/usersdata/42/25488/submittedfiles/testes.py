# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
l=input("digite o numero de linhas: ")
c=input("digite o numero de colunas: ")
a=np.zeros((l,c))
for i in range(0,a.shape[0]):
    for j in range(0,b.shape[1]):
        a[i,j]=input("linha %i coluna %i: "%(i,j))
print a
def quadrada(matriz):
    if matriz.shape[0]==matriz.shape[1]:
        return true
if quadrada(a):
    print("quadrada")
        