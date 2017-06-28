# -*- coding: utf-8 -*-
import numpy as np
def diagnalprincipal(a):
    for i in range(0,a.shape[0],1):
    soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        soma=soma-a[i,i]
        if soma<=a[i,i]:
            return False
    return True
n=int(input('Digite n: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shapee[1],1):
        a[i,j]=int(input('Digite o valor: '))
if diagonalprincipal==True:
    print('S')
else:
    print('N')
