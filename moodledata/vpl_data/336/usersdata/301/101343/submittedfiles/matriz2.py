# -*- coding: utf-8 -*-
import numpy as np
n= int(input('digite a dimensão da matriz: '))
matriz=np.empty([n,n])
for i in range (0,n,1):
    for j in range(0,n,1):
        matriz[i][j]= float(input('digite o elemento da linha%d e coluna%d: '%(i,j)))
somal=0
somac=0
somadp=0
somads=0
for i in range(0,n,1):
    for j in range(0,n,1):
        somal+=matriz[i][j]
    somal*=-1
for j in range(0,n,1):
    for i in range(0,n,1):
        somac+=matriz[i][j]
    somac*=-1
for i range(0,n,1)
    if i<(n-1):
        if matriz[i][j]==matriz[i+1][j+1]:
            somadp+=matriz[i][j]
            somadp*=-1
for i range(0,n,1)
    if i<(n-1):
        if matriz[i][i]==matriz[i+1][i+1]:
            somadp+=matriz[i][i]
            somadp*=-1
for i in range(0,n,1):
    for j in range(n-1,-1,-1):
        somads+=matriz[i][j]
    somads*=-1
print(somal)
print(somac)
print(somadp)
print (somads)
if somal==somac and somal==somadp and somal==somads:
    print('S')
if somal!=somac or somal!=somadp or somal!=somads:
    print('N')    
    
        