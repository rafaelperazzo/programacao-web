# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
n = input ('Digite a dimensão da matriz:')
x = input ('Digite o índice da posição no eixo horizontal:')
y = input ('Digite o índice da posição no eixo vertical:')
peso=0
c=0
d=0

a=np.zeros((n,n))

for i  in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Preencha a matriz:')
        
while (c<=n):
    peso = peso + a[x,c]
    c = c+1
    
while (d<=n):
    peso = peso + a[d,y]
    c = c+1
    
print (peso)
    
