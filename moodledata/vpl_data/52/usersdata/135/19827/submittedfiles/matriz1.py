# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def mr(matriz): #mr = matriz reduzida
    a=0
    for i in range(0,matriz.shape[0],1):
        if 1 in matriz[i,:]:
            a=i
            break
    b=0
    for i in range(0,matriz.shape[1],1):
        if 1 in matriz[:,i]:
            b=i
            break
    c=0
    for i in range(matriz.shape[0]-1,0,-1):
        if 1 in matriz[i,:]:
            c=i+1
            break
    d=0
    for i in range(matriz.shape[1]-1,0,-1):
        if 1 in matriz[:,i]:
            d=i+1
            break
    return matriz[a:c,b:d]

li=input("Entre com a quantidade de linhas: ")
co=input("Entre com a quantidade de colunas: ")
m=np.zeros((li,co))

print
for k in range(0,m.shape[0],1):
    for l in range(0, m.shape[1],1):
        print "Posicao linha %s, coluna %s"%(k,l)
        m[k,l]=input("Entre com o elemento: ")
    print

print mr(m)

