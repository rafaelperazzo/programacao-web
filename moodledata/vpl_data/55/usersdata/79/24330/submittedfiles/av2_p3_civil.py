# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Entrada

n = input('Dimensao da matriz : ')
x = input('Coordenada da linha: ')
y = input('Coordenada da coluna: ')

Linha = n
Coluna = n
a = np.zeros((n,n))

for i in range (0, a.shape[0], 1) :
    for j in range (0, a.shape[1], 1) :
        a[i,j] = input ('Elemento da matriz A: ')
        
smL = 0
for i in range (0, a.shape[1], 1) :
    for j in range (0, a.shape[0], 1) :
        if i == x :
            smL = smL + a[i,j]
            
smC = 0
for j in range (0, a.shape[0], 1) :
    for i in range (0, a.shape[1], 1) :
        if j == y :
            smC = smC + a[i,j]
            
smT = smL + smC
smT = smT - (2*a[x,y])


        
print ('%d' % smt)