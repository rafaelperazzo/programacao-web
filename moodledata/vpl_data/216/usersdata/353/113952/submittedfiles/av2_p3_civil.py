# -*- coding: utf-8 -*-
import numpy as np

ordem=int(input('dimensão da matriz'))
x=int(input('linha'))
y=int(input('coluna'))
matriz=np.zeros((ordem,ordem))

for i in range(0,ordem,1):
    for j in range (0,ordem,1):
        matriz[i,j]=int(input('valores da matriz'))
        
i=x
soma1=0
for j in range (0,ordem,1):
    if j!=y :
        soma1=soma1 + matriz[i,j]
j=y        
soma2=0
for i in range (0,ordem,1):
    if i!=x :
        soma2=soma2 + matriz[i,j]

peso=soma1 + soma2 

print (peso)

        
            










