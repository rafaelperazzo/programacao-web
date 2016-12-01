# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n = input('Digite a dimensão da matriz a :')
x = input('Digite a cordenada x')
y = input('Digite a cordenada y:')

linha=n
coluna=n
a=np.zeros ((linha,coluna))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('Digite os elementos da matriz:')

soma = 0
        
for i in range (0,a.shape[1],1):
    for j in range (0,a.shape[0],1):
        if i==x:
            soma = soma  + a[i,j]

soma2 = 0
for j in range (0,a.shape[0],1):
    for i in range (0,a.shape[1],1):
        if j==y:
            soma2 = soma2  + a[i,j]

smT = soma + soma2
smT = smT-(2*a[x,y])

print smT