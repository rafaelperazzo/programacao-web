# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Digite o tamanho da matriz nxn: '))
a=np.zeros( (n,n) )


for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=int(input('elemento: '))
        
for i in range (n-1,n+1):
    v=0
    if a[i,j]==a[i,j+1] and a[i,j]==a[i,j-1] and a[i,j-1]==a[i,j+1]:
        v+=1
    elif a[i,j]==a[i+1,j] and a[i,j]==a[i-1,j] and a[i+1,j]==a[i-1,j]:
        v+=1
    elif a[i,j]==a[i+1,j+1] and a[i,j]==a[i-1,j-1] and a[i+1,j+1]==a[i-1,j-1]:
        v+=1
    else: 
        v+=0

if v!=0:
    print('S')
else:
    print('N')

        
        

