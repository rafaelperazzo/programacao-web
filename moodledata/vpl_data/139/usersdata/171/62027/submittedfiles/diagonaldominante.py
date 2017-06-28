# -*- coding: utf-8 -*-
import numpy as np
def diagonaldominante(a):
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
            if i==j:
                if a[i,j]>soma:
                    cont=cont+1
        if cont==0:
            return False
        else:
            return True
n=int(input('digite o numero de linhas e coluna:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite numeros:'))
if diagonaldominante(a):
    print('SIM')
else:
    print('NAO')
