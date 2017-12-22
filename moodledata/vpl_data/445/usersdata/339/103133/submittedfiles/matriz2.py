# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Digite o tamanho da matriz nxn: '))
a=np.zeros( (n,n) )


for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=int(input('elemento: '))
sl=[]
for k in range (0,n):
    sl.append(sum(a[i]))


sc=0
for k in range (0,n):        
    sc+=(a[k][k])   
    
if (sum(sl)/n)==sc:
    print('S')
else :
    print('N')

