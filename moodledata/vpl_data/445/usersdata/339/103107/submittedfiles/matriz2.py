# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Digite o tamanho da matriz nxn: '))
m=np.zeros(n,n)
for i in range(0,n,1):
    for j in range(0,n,1):
        m[i,j]=int(input('elemento: '))
        
print(m)
        
        

