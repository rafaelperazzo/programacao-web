# -*- coding: utf-8 -*-
import numpy as np
def somaLinhas(a):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape[1],1):
            if i!=j:
                soma=soma+a[i,j]
        b.append(soma)
    return(b)

def diagonalDominante(a,b):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                if a[i,j]<b[i]:
                    return(False)
    return(True)

n=int(input('Digite a ordem da matriz: '))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um valor para o termo: '))
        
b=somaLinhas(a)

if diagonalDominante(a,b):
    print('SIM')
else:
    print('NAO')