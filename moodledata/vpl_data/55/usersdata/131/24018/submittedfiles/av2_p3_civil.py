# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np


n=input("Digite a dimensão da matriz:")
x=input("Digite a cordenada x :")
y=input("Digite a cordenada y :")

linha=n
coluna=n
a=np.zeros ((linha,coluna))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input("Digite um elemento para a matriz:")
sm1=0
for i in range (0,a.shape[1],1):
    for j in range (0,a.shape[0],1):
        if i==x:
            sm1=sm1+ a[i,j]
sm2=0
for j in range (0,a.shape[0],1):
    for i in range (0,a.shape[1],1):
        if j==y:
            sm2 = sm2  + a[i,j]

smt=sm1+sm2
smt=smt-(2*a[x,y])

print smt
    