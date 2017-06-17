# -*- coding: utf-8 -*-
import numpy as np
def diagonaldominante(a):
    for i in range(0,a,shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]-a[i,i]
        if soma<=a[i,i]:
            return False
    
    return True
    
n=int(input('digite a ordem da matriz:'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite um numero:'))
        
if diagonaldominante(a)==True:
    print('SIM')
else:
    print('NAO')
            

