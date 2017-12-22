# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Digite o tamanho da matriz nxn: '))
a=np.zeros( (n,n) )


for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=int(input('elemento: '))

sl=sum(a[i])
sc=sum(a[j])

sv=0

for k in range (0,n):
    if i==j:
        sv+=(a[i][j])

if sl==sc and sc==sv:
    print('S')
else :
    print('N')

        
        

