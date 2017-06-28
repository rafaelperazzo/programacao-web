# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Informe o número de linhass e colunas:'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Informe os elementos:'))
        
def diagonal_dominante(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return(soma)

def soma_linhas(a):
    for i in range(0,a.shape[0],1):
        s=0
        for j in range(0,a.shape[1],1):
            s=s+a[i,j]
        return (s)    
x=diagonal_dominante(a)
y=soma_linhas(a)
if x>y:
    print('S')
else:
    print('N')
        