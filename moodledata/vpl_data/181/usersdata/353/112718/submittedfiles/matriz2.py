# -*- coding: utf-8 -*-

import numpy as np
linhas=int(input())
colunas=int(input())
A=np.zeros ((linhas,colunas))

somalinha=0
somacoluna=0
somadiagonal1=0
somadiagonal2=0

    
    
for i in range (0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        somalinha=somalinha+A[i,j]
        break 
    
for j in range (0,A.shape[1],1):
    for i in range (0,A.shape[0],1):
        somacoluna=somacoluna+A[i,j]
        break

if somalinha==somacoluna==somadiagonal1==somadiagonl2 :
    print ('S')
    else:
        print ('N')

