# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Digite o tamanho da matriz nxn: '))
a=np.zeros( (n,n) )


for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=int(input('elemento: '))

sl=sum(a[i])
sc=sum(a[j])

if sl==sc:
    print('S')
else :
    print('N')

        
        

