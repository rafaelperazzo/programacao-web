# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input("Digite a dimensão da matriz:")
pdp=[]
z=2
while z>0:
    z.append(input("Digite os elementos para calcular o peso da peça:")

linha=n
coluna=n
a=np.zeros((linha,coluna))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input("Digite um elemento para a matriz:")
        
print a

