# -*- coding: utf-8 -*-
import numpy as np
def dominante(a):
    somaL=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[0],1):
            somaL=somaL+a[i,j]
        somaL=somaL-a[i,i]
        if somaL>a[i,i]:
            return False
    return True
n=0
while n<1:
    n=int(input('Digite a ordem da matriz: '))
A=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        A[i,j]=input('Digite o elemento %d%d da matriz: ' %(i,j))
if dominante(A)==False:
    print('NAO')
else:
    print('SIM')