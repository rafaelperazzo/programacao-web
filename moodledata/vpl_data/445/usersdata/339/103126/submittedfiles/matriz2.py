# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Digite o tamanho da matriz nxn: '))
a=np.zeros( (n,n) )


for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=int(input('elemento: '))

sl=sum(a[i])
sc=sum(a[j])

sv1=0
for k in range (0,n):
    if i==j:
        sv1+=(a[i][j])
        
sv2=0
for k in range (0,n):
    sv2+=(a[i][j-k])
    
if sv1==sv2:
    sv=(sv1+sv2)/2
    
if sl==sc and sc==sv:
    print('S')
else :
    print('N')

        
        

