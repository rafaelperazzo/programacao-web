# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Digite o tamanho da matriz nxn: '))
a=np.zeros( (n,n) )


for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=int(input('elemento: '))
    for l in range (0,n):
        v=0
        if a[i,j]==a[i,j+l] and a[i,j]==a[i,j-l] and a[i,j-l]==a[i,j+l]:
            v+=1
        elif a[i,j]==a[i+l,j] and a[i,j]==a[i-l,j] and a[i+l,j]==a[i-l,j]:
            v+=1
        elif a[i,j]==a[i+l,j+l] and a[i,j]==a[i-l,j-l] and a[i+l,j+l]==a[i-l,j-l]:
            v+=1
        else: 
            v+=0

if v!=0:
    print('S')
else:
    print('N')

        
        

