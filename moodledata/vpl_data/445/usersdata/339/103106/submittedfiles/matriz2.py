# -*- coding: utf-8 -*-
import numpy as np

m=[]
n=int(input('Digite o tamanho da matriz nxn: '))

for i in range(0,n,1):
    for j in range(0,n,1):
        m[i][j]=int(input('elemento: '))
        
print(m)
        
        

